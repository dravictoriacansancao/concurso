"""Provas de MÉDICO PERITO de outras bancas (data/raw_outras/) → data/outras_bruto.jsonl.

Cada banca tem um layout: marcador da questão, marcador das alternativas e se a página tem duas colunas.
O gabarito vem de gabaritos_outras.py. Itens que não batem com o gabarito são descartados e listados.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from coletar_historico import run, _soltas
import gabaritos_outras as G

RAW = G.RAW
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "outras_bruto.jsonl")

def texto(pdf, colunas, layout=False, pular=0):
    """layout=True: só pdftotext -layout por coluna (preserva a ordem visual; o modo simples embaralha o Cebraspe)."""
    import pdfplumber
    pdf = os.path.join(RAW, pdf); out = ""
    with pdfplumber.open(pdf) as doc:
        for p, pg in enumerate(doc.pages, 1):
            if p <= pular: continue
            w, h = pg.width, pg.height
            faixas = ((0, w / 2), (w / 2, w)) if colunas else ((0, w),)
            for x0, x1 in faixas:
                if layout:
                    out += "\n" + run("pdftotext", "-layout", "-f", str(p), "-l", str(p), "-x", str(int(x0)), "-y", "0", "-W", str(int(x1 - x0)), "-H", "2000", pdf, "-"); continue
                a = run("pdftotext", "-f", str(p), "-l", str(p), "-x", str(int(x0)), "-y", "0", "-W", str(int(x1 - x0)), "-H", "2000", pdf, "-")
                b = pg.crop((x0, 0, x1, h)).extract_text(x_tolerance=1.5) or ""
                out += "\n" + (a if _soltas(a) <= _soltas(b) else b)
    return out

LIXO = [r"pcimarkpci \S+", r"CONCURSOPÚBLICO\S*( \d+)?( NAL)?", r"\s*\bPROVA DE\s*$", r"\S*DO CARIRI-URCA", r"DE VESTIBULAR-CEV", r"\S*IMENTO DE CARGOS EFETIVOS", r"\S*IPIO DE VÁRZEA ALEGRE", r"\S*MDAwMDow\S*", r"\S*6MmQwNzpi\S*", r"(CONCUR)?SO PÚBLICO\s+PREFEITURA DE GOIÂNIA/20\d ?\d", r"UFG/CS( CONCUR)?", r"CEBRASPE – MPS – Edital: 2024", r"Espaço livre", r"▬ RASCUNHO ▬+", r"RASCUNHO",
        r"UFG/CS\s+CONCURSO PÚBLICO\s+PREFEITURA DE GOIÂNIA/2022", r"PREFEITURA MUNICIPAL DE MACAÉ", r"FGV CONHECIMENTO",
        r"Médico Perito\s+Tipo\s+\d+\s*–\s*Cor\s+\w+\s+Página\s+\d+", r"Página \d+", r"MÉDICO PERITO",
        r"CONCURSO PÚBLICO PARA PROVIMENTO DE CARGOS EFETIVOS DA PREFEITURA DO MUNICÍPIO DE VÁRZEA ALEGRE",
        r"UNIVERSIDADE REGION\S*( DO CARIRI-URCA)?", r"\S*EFETIVOSDAPREFEITURA\S*", r"COMISSÃO EXECUTIVA D\S*( DE VESTIBULAR-CEV)?",
        r"CONCURSO PÚBLICO PARA PROVI\S*", r"DA PREFEITURA DO MUNI\S*", r"www\.pciconcursos\.com\.br", r"-{5,}\w*", r"COMISS ?ÃO EXECUTIVA DE VESTIBULAR-CEV",
        r"CONCURSO P ?ÚBLICO PARA PROVIMENTO DE CARGOS EFETIVOS", r"DA PREFEITURA DO MUNIC ?ÍPIO DE V ?ÁRZEA ALEGRE",
        r"\d{3}_[A-Z_]+\s+\d+/\d+/\d+\s*[\d:]+", r"Execução: Fundatec", r"NOVA SANTA RITA.*", r"\(CONCURSO VÁRZEA ALEGRE / 2024\)"]

ACENTO = {"´": "\u0301", "˜": "\u0303", "ˆ": "\u0302", "`": "\u0300", "¸": "\u0327"}
def acentos(s):
    """URCA: acento como caractere solto depois da letra ('opc¸a˜o', 'Piau´i', 'VA´ RZEA')."""
    import unicodedata
    s = re.sub(r"([A-ZÇ])([´˜ˆ`¸]) (?=[A-Z])", r"\1\2", s)
    s = re.sub(r"[´`]([iı])", lambda m: "í" if m.group(0)[0] == "´" else "ì", s)
    s = re.sub(r"([A-Za-z])([´˜ˆ`¸])", lambda m: m.group(1) + ACENTO[m.group(2)], s)
    return unicodedata.normalize("NFC", s)

def limpa(s):
    s = acentos(s)
    for r in LIXO: s = re.sub(r, " ", s)
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)          # hifenização de fim de linha
    s = s.replace("ı́", "í").replace("ı", "i")
    s = re.sub(r"\s+", " ", s).strip()
    return s

# (arquivo, colunas, marcador da questão, marcador das alternativas)
BANCAS = {
    "URCA":     ("CEV-URCA_Varzea-Alegre-CE-2024_CADERNO_MEDICO_PERITO.pdf", True, r"\n\s*(\d{2})\.\s*(?=\(CONCURSO)", r"(?:^|\n)\s*([A-E])\)\s"),
    "FGV":      ("FGV_Macae-RJ-2024_CADERNO_MEDICO_PERITO.pdf", True, r"\n\s*(\d{1,2})\s*\n", r"(?:^|\n)\s*\(([A-E])\)\s"),
    "FUNDATEC": ("FUNDATEC_Nova-Santa-Rita-RS-2023_CADERNO_MEDICO_PERITO_PSIQUIATRA.pdf", False, r"\n\s*QUESTÃO\s+(\d{2})\s*[–-]", r"(?:^|\n)\s*([A-E])\)\s"),
    "UNIFIL":   ("INSTITUTO-UNIFIL_Paranagua-PR-2022_CADERNO_MEDICO_PERITO.pdf", True, r"\n\s*(\d{1,2})\.\s", r"(?:^|\n)\s*([a-d])\)\s"),
    "UFG":      ("UFG_Goiania-GO-2022_CADERNO_MEDICO_PERITO.pdf", True, r"▬\s*QUESTÃO\s+(\d{2})\s*▬+", r"(?:^|\n)\s*\(([A-D])\)\s"),
    "UPENET":   ("UPENET-IAUPE_Olinda-PE-2024_CADERNO_MEDICO_PERITO.pdf", False, r"\n\s*(\d{2})\.\s", r"(?:^|\s)([A-E])\)\s"),
}
PULAR = {"UNIFIL": 1}   # capa com instruções numeradas
META = {
    "URCA":     dict(banca="CEV-URCA", municipio="Várzea Alegre", uf="CE", ano=2024, cargo="Médico Perito", gab=G.urca),
    "FGV":      dict(banca="FGV", municipio="Macaé", uf="RJ", ano=2024, cargo="Médico Perito", gab=G.fgv),
    "FUNDATEC": dict(banca="FUNDATEC", municipio="Nova Santa Rita", uf="RS", ano=2023, cargo="Médico Perito Psiquiatra", gab=G.fundatec),
    "UNIFIL":   dict(banca="Instituto UniFil", municipio="Paranaguá", uf="PR", ano=2022, cargo="Médico Perito", gab=G.unifil),
    "UFG":      dict(banca="UFG/CS", municipio="Goiânia", uf="GO", ano=2022, cargo="Médico Perito", gab=G.ufg),
    "UPENET":   dict(banca="UPENET/IAUPE", municipio="Olinda", uf="PE", ano=2024, cargo="Médico Perito", gab=G.olinda),
}

def sequencial(cad, marcador, total):
    """Corta nos marcadores aceitando só a numeração crescente 1, 2, 3… (descarta números soltos no meio do texto)."""
    partes = re.split(marcador, "\n" + cad)
    qs, esperado, atual = {}, 1, None
    for k in range(1, len(partes) - 1, 2):
        n = int(partes[k])
        if n == esperado and n <= total:
            atual = n; qs[n] = partes[k + 1]; esperado += 1
        elif atual:
            qs[atual] += "\n" + partes[k] + "\n" + partes[k + 1]
    return qs

def multipla(chave):
    pdf, colunas, marc, alt = BANCAS[chave]; meta = META[chave]
    g = meta["gab"](); prelim = False
    if isinstance(g, tuple): g, tipo = g; prelim = tipo == "preliminar"
    cad = texto(pdf, colunas, layout=chave == "UNIFIL", pular=PULAR.get(chave, 0))
    letras = "ABCDE" if chave in ("URCA", "FGV", "FUNDATEC", "UPENET") else "ABCD"
    itens, ruins = [], []
    for n, corpo in sequencial(cad, marc, max(g)).items():
        partes = re.split(alt, "\n" + corpo)
        enun = limpa(partes[0])
        alts = {}
        for j in range(1, len(partes) - 1, 2):
            L = partes[j].upper()
            if L not in alts: alts[L] = limpa(partes[j + 1])
        # a última alternativa leva junto o texto-base da próxima questão: corta em linha de título/“Texto”
        ultima = letras[-1]
        if ultima in alts:
            alts[ultima] = re.split(r"\s(?:[Tt][Ee][Xx][Tt][Oo]\s+\d|Leia o texto|Instrução:|LÍNGUA PORTUGUESA|CONHECIMENTOS|MÓDULO|Língua Portuguesa|Legislação|Conhecimentos)", alts[ultima])[0].strip()
        if sorted(alts) != list(letras) or g.get(n) not in list(letras) + ["ANULADA"]:
            ruins.append((n, sorted(alts), g.get(n))); continue
        itens.append(dict(fonte=pdf, banca=meta["banca"], municipio=meta["municipio"], uf=meta["uf"], ano=meta["ano"],
                          cargo=meta["cargo"], numero=n, enunciado=enun, alternativas=alts, gabarito=g[n],
                          anulada=g[n] == "ANULADA", formato="A-" + letras[-1], preliminar=prelim))
    return itens, ruins, len(g)

def cebraspe(parte):
    pdf = f"CEBRASPE_MPS-Perito-Medico-Federal-BR-2025_CADERNO_MEDICO_PERITO_{parte}.pdf"
    g = G.cebraspe(parte); cad = texto(pdf, True, layout=True)
    partes = re.split(r"\n\s*(\d{1,3})\s+(?=\S)", "\n" + cad)
    corpos, esperado, atual = {}, min(g), None
    for k in range(1, len(partes) - 1, 2):
        n = int(partes[k])
        if n == esperado: atual = n; corpos[n] = partes[k + 1]; esperado += 1
        elif atual: corpos[atual] += "\n" + partes[k] + " " + partes[k + 1]
    # o texto entre itens que traz "julgue" é o comando/situação do bloco seguinte
    itens, contexto = [], ""
    inicio = re.split(r"\n\s*%d\s+" % min(g), cad, 1)[0]
    m = list(re.finditer(r"\n\s*\n", inicio)); contexto = limpa(inicio[m[-1].end():] if m else inicio)
    contexto = contexto[contexto.rfind("julgue") - 300:] if len(contexto) > 1500 else contexto
    for n in sorted(corpos):
        corpo = corpos[n]; prox = ""
        j = re.search(r"julgue", corpo, re.I)
        if j:
            antes = corpo[:j.start()]
            cortes = [c.end() for c in re.finditer(r"\.\s*\n", antes)]
            vazios = [c.start() for c in re.finditer(r"\n\s*\n", antes)]
            corte = (vazios[0] if vazios else cortes[0] if cortes else j.start())
            corpo, prox = corpo[:corte], corpo[corte:]
        if n in g and g[n] in ("C", "E", "ANULADA"):
            itens.append(dict(fonte=pdf, banca="Cebraspe", municipio="MPS", uf="BR", ano=2025,
                              cargo="Perito Médico Federal", numero=n, contexto=contexto, enunciado=limpa(corpo),
                              alternativas={"C": "Certo", "E": "Errado"}, gabarito=g[n], anulada=g[n] == "ANULADA",
                              formato="C/E", preliminar=False))
        if prox: contexto = re.sub(r"^.*?--\s*|^.*\bmando que imediatamente o antecede\..*$", "", limpa(prox)).strip()
    return itens, [n for n in g if n not in corpos], len(g)

if __name__ == "__main__":
    todos = []
    for chave in list(BANCAS) + ["CEB-G", "CEB-E"]:
        it, ruins, tot = cebraspe({"CEB-G": "ConhecGerais", "CEB-E": "ConhecEspecificos"}[chave]) if chave.startswith("CEB") else multipla(chave)
        print(f"{chave:<9} {len(it):>3}/{tot}  descartadas: {ruins[:12]}")
        todos += it
    with open(OUT, "w") as f:
        for q in todos: f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(len(todos), "itens →", OUT)
