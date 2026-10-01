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
    (6, "MEDICO DE SAUDE DO TRABALHO"): r"^MÉDICO DE SAÚDE DO TRABALHO$", (6, "MEDICO PSIQUIATRA"): r"^MÉDICO PSIQUIATRA$",
    (17, "MEDICO PSF"): r"^MÉDICO – PSF$", (17, "MEDICO PLANTONISTA"): r"^MÉDICO – PLANTONISTA$",
    (20, "MEDICO CLINICO GERAL"): r"^MÉDICO CLÍNICO GERAL$",
    **{(21, f"MEDICO {c}"): rf"^MÉDICO {c}$" for c in ("CARDIOLOGISTA", "PLANTONISTA", "PSIQUIATRA", "ORTOPEDISTA", "PEDIATRA")},
    (64, "MEDICO CLINICO GERAL"): r"^SUP - MÉDICO CLÍNICO GERAL$",
    (74, "MEDICO CLINICO GERAL"): r"^T40 - MÉDICO \(A\) CLÍNICO \(A\) GERAL T40$", (74, "MEDICO PEDIATRA"): r"^MDP - MÉDICO \(A\) PEDIATRA$",
    (77, "MEDICO PSIQUIATRA"): r"^MÉDICO PSIQUIATRA$", (77, "MEDICO PEDIATRA"): r"^MÉDICO PEDIATRA$",
    (77, "MEDICO PSF"): r"^MÉDICO \(PSF\)$", (77, "MEDICO CLINICO"): r"^MÉDICO \(CLÍNICO\)$",
    (89, "MEDICO CLINICO"): r"^MDC - MÉDICO CLÍNICO PLANTONISTA$", (89, "MEDICO UROLOGISTA"): r"^MDC - MÉDICO UROLOGISTA$",
    (110, "MEDICO CARDIOLOGISTA"): r"^SUP - MÉDICO CARDIOLOGISTA$", (110, "MEDICO PSIQUIATRA"): r"^SUP - MÉDICO PSIQUIATRA$",
    (121, "MEDICO ANGIOLOGISTA VASCULAR"): r"^MÉDICO ANGIOLOGISTA / VASCULAR$", (121, "MEDICO CARDIOLOGISTA"): r"^MÉDICO CARDIOLOGISTA$",
    (121, "MEDICO PEDIATRA"): r"^MÉDICO PEDIATRA$", (121, "MEDICO UROLOGISTA"): r"^MÉDICO UROLOGISTA$",
    (121, "MEDICO NEUROPEDIATRA"): r"^NEUROPEDIATRA$", (121, "MEDICO OTORRINOLARINGOLOGISTA"): r"^OTORRINOLARINGOLOGISTA$",
    (122, "MEDICO PLANTONISTA"): r"^MÉDICO PLANTONISTA$", (129, "MEDICO PSF"): r"^MÉDICO PSF$", (133, "MEDICO PSF"): r"^MÉDICO - PSF$",
    (136, "MEDICO PLANTONISTA"): r"^MÉDICO PLANTONISTA$", (136, "MEDICO PSF"): r"^MÉDICO PSF$",
    (137, "MEDICO NEUROLOGISTA"): r"^NEUROLOGISTA$", (137, "MEDICO CARDIOLOGISTA CLINICO"): r"^CARDIOLOGISTA CLÍNICO$",
    (137, "MEDICO ENDOCRINOLOGISTA E METABOLOGIA"): r"^ENDOCRINOLOGISTA E METABOLOGIA$",
    (143, "MEDICO"): r"^MÉDICO$", (143, "MEDICO PLANTONISTA"): r"^MÉDICO PLANTONISTA$", (143, "MEDICO DO PSF"): r"^MÉDICO DO PSF$",
    (155, "MEDICO ESF"): r"^SUP - MÉDICO \(ESF\)$", (155, "MEDICO NEUROPEDIATRA PSIQUIATRA INFANTIL"): r"^SUP - NEUROPEDIATRA / PSIQUIATRA INFANTIL$",
    (164, "MEDICO PLANTONISTA"): r"^MÉDICO PLANTONISTA$",
}

def run(*a): return subprocess.run(list(a), capture_output=True, text=True).stdout
def npag(p): return int(re.search(r"Pages:\s+(\d+)", run("pdfinfo", p)).group(1))

PAR = re.compile(r"\b(\d{2})[.:]\s*([A-E]|V|F|Anulad[ao])\b", re.I)

def gabarito_oficial(pdf, regex):
    linhas = run("pdftotext", "-layout", pdf, "-").split("\n")
    for i, l in enumerate(linhas):
        if re.search(regex, re.sub(r"\s+", " ", l.strip().upper())):
            g = {}
            for l2 in linhas[i + 1:]:
                pares = PAR.findall(l2)
                if len(pares) < 2:
                    if l2.strip() and g: break
                    continue
                g.update({int(n): ("ANULADA" if v.upper().startswith("ANULAD") else v.upper()) for n, v in pares})
            if g:
                return g
    raise SystemExit(f"{os.path.basename(pdf)}: rótulo {regex} não encontrado")

def _soltas(t):
    toks = t.split()
    return sum(len(x) == 1 and x.isalpha() and x not in "aeoAEOéÉàÀ" for x in toks) / max(1, len(toks))

def texto_caderno(pdf):
    import pdfplumber
    out = ""
    with pdfplumber.open(pdf) as doc:
        for p, pg in enumerate(doc.pages, 1):
            w, h = pg.width, pg.height
            for x0, x1 in ((0, w / 2), (w / 2, w)):
                a = run("pdftotext", "-f", str(p), "-l", str(p), "-x", str(int(x0)), "-y", "0", "-W", str(int(x1 - x0)), "-H", "900", pdf, "-")
                b = pg.crop((x0, 0, x1, h)).extract_text(x_tolerance=1.5) or ""
                out += "\n" + (a if _soltas(a) <= _soltas(b) else b)
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

def itens_vf(cad):
    """Formato 'Julgue os itens': 'NN. afirmação' sem alternativas; números crescentes."""
    qs, esperado = {}, 1
    partes = re.split(r"\n\s*(\d{2})\.\s+", "\n" + cad)
    atual = None
    for k in range(1, len(partes) - 1, 2):
        n = int(partes[k])
        if n == esperado:
            atual = n; qs[n] = partes[k + 1]; esperado += 1
        elif atual:
            qs[atual] += f"\n{partes[k]}. " + partes[k + 1]
    return {n: (limpa(t), {"V": "Verdadeiro (certo)", "F": "Falso (errado)"}) for n, t in qs.items()}

def main():
    out = []
    for cad in sorted(glob.glob(os.path.join(RAW, "IGEDUC_*_CADERNO_*.pdf"))):
        nome = os.path.basename(cad)
        m = re.match(r"IGEDUC_(\d+)_(.+?)-([A-Z]{2})-(\d{4})_CADERNO_(.+)\.pdf", nome)
        cid, mun, uf, ano, cargo = int(m[1]), m[2].replace("_", " "), m[3], int(m[4]), m[5].replace("_", " ")
        gab_pdf = sorted(glob.glob(os.path.join(RAW, f"IGEDUC_{cid}_*_GABARITO_*.pdf")))[0]
        gab = gabarito_oficial(gab_pdf, ROTULO[(cid, cargo)])
        txt = texto_caderno(cad)
        vf = set(gab.values()) <= {"V", "F", "ANULADA"}
        qs = itens_vf(txt) if vf else questoes(txt)
        pos = max(txt.find("Conhecimentos Específicos"), txt.find("CONHECIMENTOS ESPECÍFICOS"))
        m_esp = re.search(r"Questão\s+(\d{2})|\n\s*(\d{2})\.\s", txt[pos:]) if pos > 0 else None
        n_esp = int(m_esp.group(1) or m_esp.group(2)) if m_esp else None
        faltam = sorted(set(gab) - set(qs))
        for n in sorted(qs):
            e, a = qs[n]
            out.append(dict(fonte=nome, concurso=cid, municipio=re.sub(r"(?<=[a-z])(?=[A-Z])", " ", mun), uf=uf, ano=ano,
                            cargo=cargo, numero=n, grupo="Específicos" if n_esp and n >= n_esp else "Gerais",
                            enunciado=e, alternativas=dict(sorted(a.items())), gabarito=gab.get(n),
                            anulada=gab.get(n) == "ANULADA", gabarito_fonte=os.path.basename(gab_pdf),
                            formato="V/F" if vf else f"{len(a)} alternativas", preliminar="PRELIMINAR" in gab_pdf))
        print(f"{nome[:62]:<62} {len(qs)} q · gabarito {len(gab)} · 1ª específica {n_esp} · sem texto: {faltam}")
    with open(os.path.join(BASE, "data", "historico_bruto.jsonl"), "w", encoding="utf-8") as f:
        for q in out: f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print("total extraído:", len(out))

if __name__ == "__main__":
    main()
