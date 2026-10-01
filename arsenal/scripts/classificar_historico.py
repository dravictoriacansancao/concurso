"""Etapa 2b: deduplica (mesma questão em vários cargos do mesmo concurso) e classifica na taxonomia do edital.
Entrada: data/historico_bruto.jsonl · Saída: data/historico.jsonl"""
import json, os, re
from difflib import SequenceMatcher
BASE = os.path.join(os.path.dirname(__file__), "..")
FORA = "fora do edital"
N = lambda s: re.sub(r"\W+", "", s.lower())

def has(t, *ws): return any(re.search(w, t, re.I) for w in ws)

def port_sub(e):
    if has(e, r"acentua|ortogra|s[íi]laba|d[íi]grafo|fonema"): return "Fonologia"
    if has(e, r"concord[âa]ncia|reg[êe]ncia|crase|pontua[çc][ãa]o|sint[áa]tic|coloca[çc][ãa]o pronominal|ora[çc][ãa]o subordinada"): return "Sintaxe"
    if has(e, r"classe gramatical|voc[áa]bulos? \"que\"|morfol|forma[çc][ãa]o de palavras"): return "Morfologia"
    if has(e, r"figura de linguagem|denota|conota|sin[ôo]nim"): return "Semântica"
    if has(e, r"of[íi]cio|reda[çc][ãa]o oficial|memorando"): return "Redação Oficial"
    return "Interpretação e Análise Textual"

def info_sub(t):
    regras = [
        (r"Excel|planilha|c[ée]lula|PROCV|SOMASE|CONT\.SE|Calc\b", "Utilização de planilhas eletrônicas"),
        (r"\bWord\b|PowerPoint|Writer\b|Impress\b|marcadores e numera|editor de texto", "Aplicativos de escritório"),
        (r"malware|v[íi]rus|ransomware|phishing|engenharia social|senha|firewall|antiv[íi]rus|VPN|criptograf|autentica[çc][ãa]o|LGPD|spyware|seguran[çc]a", "Conceitos de segurança da informação e proteção de dados"),
        (r"backup|ponto de restaura", "Ferramentas de backup e recuperação de dados"),
        (r"e-mail|correio eletr|POP3|IMAP|SMTP|\bCCO\b", "E-mail e comunicação eletrônica no ambiente corporativo"),
        (r"HTTPS?\b|SSL|TLS|protocolo|\bTCP\b|\bDNS\b", "Conceitos sobre protocolos de comunicação na internet"),
        (r"Windows|Linux|macOS|sistema operacional|teclas? de atalho|Explorador de Arquivos", "Conceitos de sistemas operacionais"),
        (r"navegador|Chrome|Firefox|Edge\b|buscador|mecanismo de busca", "Conceitos sobre navegadores e ferramentas de busca"),
        (r"nuvem|cloud|SaaS|IaaS|OneDrive", "Noções de computação em nuvem"),
        (r"redes sociais|netiqueta|etiqueta digital|colaborativ|Teams|videoconfer", "Conceitos sobre redes sociais e ferramentas colaborativas"),
        (r"hardware|software|esta[çc][ãa]o de trabalho|mem[óo]ria RAM|processador|perif[ée]ric", "Conceitos básicos de hardware e software"),
    ]
    for rx, tema in regras:
        if has(t, rx): return tema
    return FORA

def legal(e):
    """Bloco de legislação/SUS/Constituição/ética (classifica pelo enunciado)."""
    if has(e, r"controle externo|Tribunal de Contas|Presidente da Rep|Poder (Executivo|Legislativo|Judici)"): return "Constitucional", "Organização dos Poderes"
    if has(e, r"princ[íi]pios constitucionais da Administra|Constitui[çc][ãa]o") and not has(e, r"\bSUS\b|Sistema Único|sa[úu]de"):
        if has(e, r"nacionalidade|direitos sociais|garantias"): return "Constitucional", "Direitos e garantias fundamentais"
        if has(e, r"efic[áa]cia imediata|aplicabilidade|direitos individuais"): return "Constitucional", "Aplicabilidade e interpretação das normas"
        if has(e, r"federativ|autonomia pol"): return "Constitucional", "Federalismo e organização do Estado"
        if has(e, r"fundamentos|objetivos fundamentais"): return "Constitucional", "Princípios fundamentais"
        return "Constitucional", "Administração Pública na CF"
    if has(e, r"\b[ée]tic|servidor p[úu]blico|probidade|moral"): return "Ética e serviço público", FORA
    if has(e, r"Biosseguran|humaniza"): return "SUS", FORA
    if has(e, r"Conselho (Municipal|Nacional|de) Sa[úu]de|Confer[êe]ncia de Sa[úu]de|controle social|8\.142"): return "SUS", "Controle social"
    if has(e, r"financiamento|Fundo (Nacional|Municipal) de Sa|LC 141"): return "SUS", "Financiamento"
    if has(e, r"NASF|Sa[úu]de da Fam[íi]lia|Aten[çc][ãa]o (B[áa]sica|Prim[áa]ria)|PNAB|agente comunit"): return "SUS", "APS e ESF"
    if has(e, r"indicador|monitoramento"): return "SUS", "Indicadores e monitoramento"
    if has(e, r"art\. ?1[5-9]\b|educa[çc][ãa]o permanente|Laborat[óo]rio|atendimento em servi[çc]os|compet[êe]ncia"): return "SUS", "Gestão municipal do SUS"
    if has(e, r"\bSUS\b|Sistema Único|8\.080"): return "SUS", "Lei nº 8.080/1990"
    return None

# correções manuais após revisão (representante de cada questão única)
AJUSTE = {
    (142, "ENFERMEIRO DO PSF", 10): ("Constitucional", "Administração Pública na CF"),
    (142, "ENFERMEIRO DO PSF", 14): ("Constitucional", "Direitos e garantias fundamentais"),
    (142, "ENFERMEIRO DO PSF", 21): ("Constitucional", "Administração Pública na CF"),
    (142, "ENFERMEIRO DO PSF", 26): ("Informática", "Conceitos sobre redes sociais e ferramentas colaborativas"),
    (142, "ENFERMEIRO DO PSF", 27): ("Informática", "Conceitos básicos de hardware e software"),
    (142, "ENFERMEIRO DO PSF", 28): ("Informática", FORA),
    (114, "FARMACEUTICO BIOQUIMICO", 38): ("SUS", "Gestão municipal do SUS"),
    (114, "FARMACEUTICO BIOQUIMICO", 40): ("SUS", "Lei nº 8.080/1990"),
}

def classifica(q):
    if (q["concurso"], q["cargo"], q["numero"]) in AJUSTE: return AJUSTE[(q["concurso"], q["cargo"], q["numero"])]
    e, n = q["enunciado"], q["numero"]; t = e + " " + " ".join(q["alternativas"].values())
    if q["concurso"] in (95, 114):            # 1–10 Port · 11–20 Inf · 21–35 específicas · 36–40 legislação
        if n <= 10: return "Português", port_sub(e)
        if n <= 20: return "Informática", info_sub(t)
        if n <= 35: return "Específica (outro cargo)", FORA
        return legal(e) or ("Específica (outro cargo)", FORA)
    # 142: caderno só de conhecimentos gerais
    r = legal(e)
    if r: return r
    i = info_sub(t)
    if i != FORA or has(e, r"Intelig[êe]ncia Artificial|assistente de tecnologia"): return "Informática", i
    return "Português", port_sub(e)

def comando(e):
    if re.search(r"\bV\b.*\bF\b|sequ[êe]ncia correta", e): return "V/F ou sequência"
    if re.search(r"proposi[çc][õo]es|afirmativas? (I|II)\b|\bI, II\b", e): return "afirmativas I-II-III"
    if re.search(r"INCORRET|\bNÃO\b|EXCETO", e): return "INCORRETA"
    return "CORRETA"

def tipo(e):
    return "situacional" if re.search(r"^(Um|Uma|Em um|Em uma|Durante|Ao |[A-Z][a-z]+ é |[A-Z][a-z]+, \d+ anos)|paciente de \d+|\d+ anos,|trabalhador", e) else "direto"

def main():
    bruto = [json.loads(l) for l in open(os.path.join(BASE, "data", "historico_bruto.jsonl"), encoding="utf-8")]
    unicas = []
    for q in bruto:
        alts = " ".join(sorted(N(v) for v in q["alternativas"].values()))
        par = None
        for u in unicas:
            if u["concurso"] == q["concurso"] and u["_en"] == N(q["enunciado"]) and SequenceMatcher(None, u["_alts"], alts).ratio() >= 0.85:
                par = u; break
        if par:
            par["cargos"].append(f"{q['cargo']} Q{q['numero']}")
            assert q["anulada"] or par["anulada"] or SequenceMatcher(None, N(par["alternativas"][par["gabarito"]]), N(q["alternativas"][q["gabarito"]])).ratio() > 0.8, (q["cargo"], q["numero"])
            continue
        q = dict(q, _en=N(q["enunciado"]), _alts=alts, cargos=[f"{q['cargo']} Q{q['numero']}"])
        unicas.append(q)
    out = []
    for q in unicas:
        d, t = classifica(q)
        out.append({**{k: v for k, v in q.items() if not k.startswith("_")}, "disciplina": d, "tema": t,
                    "tipo_enunciado": tipo(q["enunciado"]), "comando": comando(q["enunciado"]),
                    "norma_citada": sorted(set(re.findall(r"Lei n?º? ?[\d.]+/\d{4}|art\. ?\d+", q["enunciado"])))})
    with open(os.path.join(BASE, "data", "historico.jsonl"), "w", encoding="utf-8") as f:
        for q in out: f.write(json.dumps(q, ensure_ascii=False) + "\n")
    from collections import Counter
    print(f"historico.jsonl: {len(out)} questões únicas (de {len(bruto)} extraídas)")
    print(Counter(q["disciplina"] for q in out))

if __name__ == "__main__":
    main()
