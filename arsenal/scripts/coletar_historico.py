"""Etapas 1–2: extrai as questões dos cadernos IGEDUC em data/raw/ e cruza com o gabarito definitivo oficial.

Arquivos esperados em data/raw/:
  IGEDUC_<id>_<Municipio>-<UF>-<ano>_CADERNO_<CARGO>.pdf
  IGEDUC_<id>_<Municipio>-<UF>-<ano>_GABARITO_DEFINITIVO.pdf
Saída: data/historico_bruto.jsonl (uma linha por questão de cada caderno, antes da deduplicação).
"""
import glob, json, os, re, subprocess
BASE = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(BASE, "data", "raw")

# rótulo do cargo no gabarito oficial (regex sobre a linha em maiúsculas)
ROTULO = {
    (95, "ENFERMEIRO"): r"^SUP4 - ENFERMEIRO$", (95, "FISIOTERAPEUTA"): r"^SUP6 - FISIOTERAPEUTA$",
    (95, "MEDICO CLINICO GERAL"): r"^SUP7 - MÉDICO CLÍNICO GERAL$", (95, "NUTRICIONISTA"): r"^SUP8 - NUTRICIONISTA$",
    (95, "PSICOLOGO"): r"^SUP9 - PSICÓLOGO$",
    (114, "MEDICO"): r"^S11 - MÉDICO$", (114, "FARMACEUTICO BIOQUIMICO"): r"^S6 - FARMACÊUTICO/BIOQUÍMICO$",
    (142, "ENFERMEIRO DO PSF"): r"^ENFERMEIRO DO PSF \(SEC\. MUN\. DE SAÚDE\)$",
    (142, "FARMACEUTICO"): r"^FARMACÊUTICO \(SEC\. MUN\. DE SAÚDE\)$",
    (142, "MEDICO CLINICO DIARISTA"): r"^MÉDICO CLÍNICO DIARISTA \(SEC\. MUN\. DE SAÚDE\)$",
    (142, "MEDICO DO PSF"): r"^MÉDICO DO PSF \(SEC\. MUN\. DE SAÚDE\)$",
    (142, "MEDICO DO TRABALHO"): r"^MÉDICO DO TRABALHO \(SEC\. MUN\. DE SAÚDE\)$",
    (142, "MEDICO PSIQUIATRA"): r"^MÉDICO PSIQUIATRA \(SEC\. MUN\. DE SAÚDE\)$",
}

def run(*a): return subprocess.run(list(a), capture_output=True, text=True).stdout
def npag(p): return int(re.search(r"Pages:\s+(\d+)", run("pdfinfo", p)).group(1))

def gabarito_oficial(pdf, regex):
    linhas = run("pdftotext", "-layout", pdf, "-").split("\n")
    achados = []
    for i, l in enumerate(linhas):
        if re.search(regex, re.sub(r"\s+", " ", l.strip().upper())):
            g = {}
            for l2 in linhas[i + 1:]:
                pares = re.findall(r"\b(\d{2}):\s*([A-E]|Anulada)\b", l2, re.I)
                if not pares:
                    if l2.strip() and g: break
                    continue
                g.update({int(n): v.upper() for n, v in pares})
            achados.append(g)
    if len(achados) != 1:
        raise SystemExit(f"{os.path.basename(pdf)}: rótulo {regex} encontrado {len(achados)} vezes")
    return achados[0]

def texto_caderno(pdf):
    out = ""
    for p in range(1, npag(pdf) + 1):
        for x, w in ((0, 298), (298, 300)):
            out += "\n" + run("pdftotext", "-f", str(p), "-l", str(p), "-x", str(x), "-y", "0", "-W", str(w), "-H", "900", pdf, "-")
    return out

def limpa(s):
    s = re.sub(r"\n(Conhecimentos (Gerais|Específicos)|RASCUNHO|NÃO DESTAQUE|\d{1,2})\s*(?=\n|$)", "\n", s)
    s = re.sub(r"\n[^\n]*-\s*\d\s*\n", "\n", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.split(r"\s(?:PREFEITURA|RASCU\w*|NÃO DES\w*|DO CABO DE|SANTO AG|GOSTINHO|STAQUE)\b", s)[0]   # marca d'água
    s = re.sub(r"\s+(MÉDICO|FARMAC|ENFERM|FISIOT|NUTRIC|PSIC)[A-ZÁÉÍÓÚÂÊÔÃÕÇ/().\s]* - \d+$", "", s)          # rodapé "CARGO - 1"
    return s.strip()

def questoes(cad):
    partes = re.split(r"\n\s*Questão\s+(\d{2})\s*\n", "\n" + cad)
    qs = {}
    for k in range(1, len(partes) - 1, 2):
        n, corpo = int(partes[k]), partes[k + 1]
        alts = re.split(r"\n\s*\(([A-E])\)\s*", "\n" + corpo)
        qs[n] = (limpa(alts[0]), {alts[j]: limpa(alts[j + 1]) for j in range(1, len(alts) - 1, 2)})
    return qs

def main():
    out = []
    for cad in sorted(glob.glob(os.path.join(RAW, "IGEDUC_*_CADERNO_*.pdf"))):
        nome = os.path.basename(cad)
        m = re.match(r"IGEDUC_(\d+)_(.+?)-([A-Z]{2})-(\d{4})_CADERNO_(.+)\.pdf", nome)
        cid, mun, uf, ano, cargo = int(m[1]), m[2], m[3], int(m[4]), m[5].replace("_", " ")
        gab_pdf = glob.glob(os.path.join(RAW, f"IGEDUC_{cid}_*_GABARITO_DEFINITIVO.pdf"))[0]
        gab = gabarito_oficial(gab_pdf, ROTULO[(cid, cargo)])
        txt = texto_caderno(cad)
        qs = questoes(txt)
        pos = txt.find("Conhecimentos Específicos")
        n_esp = int(re.search(r"Questão\s+(\d{2})", txt[pos:]).group(1)) if pos > 0 else None
        faltam = sorted(set(gab) - set(qs))
        for n in sorted(qs):
            e, a = qs[n]
            out.append(dict(fonte=nome, concurso=cid, municipio=re.sub(r"(?<=[a-z])(?=[A-Z])", " ", mun), uf=uf, ano=ano,
                            cargo=cargo, numero=n, grupo="Específicos" if n_esp and n >= n_esp else "Gerais",
                            enunciado=e, alternativas=dict(sorted(a.items())), gabarito=gab.get(n),
                            anulada=gab.get(n) == "ANULADA", gabarito_fonte=os.path.basename(gab_pdf)))
        print(f"{nome[:62]:<62} {len(qs)} q · gabarito {len(gab)} · 1ª específica {n_esp} · sem texto: {faltam}")
    with open(os.path.join(BASE, "data", "historico_bruto.jsonl"), "w", encoding="utf-8") as f:
        for q in out: f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print("total extraído:", len(out))

if __name__ == "__main__":
    main()
