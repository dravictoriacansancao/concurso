"""Etapa 2: extrai questões dos cadernos IGEDUC (data/raw/*.pdf), cruza com o gabarito definitivo
e grava data/historico_bruto.jsonl (ainda sem classificação de tema)."""
import glob, json, os, re, subprocess
BASE = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(BASE, "data", "raw")

def pdftext(path, page, x=None, w=None):
    cmd = ["pdftotext", "-f", str(page), "-l", str(page)]
    if x is not None:
        cmd += ["-x", str(int(x)), "-y", "0", "-W", str(int(w)), "-H", "900"]
    cmd += [path, "-"]
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def npaginas(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))

def meta(nome):
    m = re.match(r"IGEDUC_(\d+)_(.+?)-([A-Z]{2})-(\d{4})_(.+)_cadernogabarito\.pdf", nome)
    cid, mun, uf, ano, cargo = m.groups()
    return dict(concurso=int(cid), municipio=re.sub(r"(?<=[a-z])(?=[A-Z])", " ", mun), uf=uf, ano=int(ano),
                cargo=cargo.replace("_", " "))

def parse_gabarito_transcrito(txt):
    m = re.search(r"GABARITO DEFINITIVO\n(.*?)Total:", txt, re.S)
    if not m:
        return None
    return {int(n): v.upper() for n, v in re.findall(r"\b(\d{2}):\s*([A-E]|ANULADA)\b", m.group(1), re.I)}

def parse_gabarito_oficial(txt, rotulos):
    linhas = txt.split("\n")
    for i, l in enumerate(linhas):
        lu = re.sub(r"\s+", " ", l.strip().upper())
        if any(lu == r or lu.endswith("- " + r) or lu.startswith(r + " (") for r in rotulos):
            g = {}
            for l2 in linhas[i + 1:]:
                pares = re.findall(r"\b(\d{2}):\s*([A-E]|Anulada)\b", l2, re.I)
                if not pares:
                    if l2.strip() and g:
                        break
                    continue
                g.update({int(n): v.upper() for n, v in pares})
            return g
    return None

def questoes(caderno):
    partes = re.split(r"\n\s*Questão\s+(\d{2})\s*\n", "\n" + caderno)
    qs = {}
    for k in range(1, len(partes) - 1, 2):
        n = int(partes[k]); corpo = partes[k + 1]
        corpo = re.sub(r"\n[^\n]*-\s*1\s*\n", "\n", corpo)            # rodapé "CARGO - 1"
        alts = re.split(r"\n\s*\(([A-E])\)\s*", "\n" + corpo)
        enun = alts[0]
        ad = {}
        for j in range(1, len(alts) - 1, 2):
            ad[alts[j]] = alts[j + 1]
        qs[n] = (enun, ad)
    return qs

def limpa(s):
    s = re.sub(r"\n(Conhecimentos (Gerais|Específicos)|RASCUNHO|NÃO DESTAQUE|\d{1,2})\s*(?=\n|$)", "\n", s)
    return re.sub(r"\s+", " ", s).strip()

def main():
    out = []
    for path in sorted(glob.glob(os.path.join(RAW, "IGEDUC_*_cadernogabarito.pdf"))):
        nome = os.path.basename(path); md = meta(nome)
        cad, gabtxt, secoes = "", "", []
        for p in range(1, npaginas(path) + 1):
            full = pdftext(path, p)
            if "GABARITO DEFINITIVO" in full:
                gabtxt += full + "\n"; continue
            esq, dir_ = pdftext(path, p, 0, 298), pdftext(path, p, 298, 300)
            cad += "\n" + esq + "\n" + dir_
        # seções Conhecimentos Gerais / Específicos: marca posição
        g_tr = parse_gabarito_transcrito(gabtxt)
        rot = [md["cargo"], md["cargo"].replace(" DO ", " DO ")]
        g_of = parse_gabarito_oficial(gabtxt, [r.upper() for r in rot])
        gab = g_of or g_tr
        conflito = [n for n in (g_tr or {}) if g_of and g_of.get(n) != g_tr.get(n)]
        qs = questoes(cad)
        # índice da 1ª questão de Conhecimentos Específicos
        pos_esp = cad.find("Conhecimentos Específicos")
        n_esp = None
        if pos_esp > 0:
            m = re.search(r"Questão\s+(\d{2})", cad[pos_esp:])
            n_esp = int(m.group(1)) if m else None
        for n in sorted(qs):
            enun, ad = qs[n]
            out.append(dict(fonte=nome, **md, numero=n,
                            grupo="Específicos" if n_esp and n >= n_esp else "Gerais",
                            enunciado=limpa(enun), alternativas={k: limpa(v) for k, v in sorted(ad.items())},
                            gabarito=(gab or {}).get(n), anulada=(gab or {}).get(n) == "ANULADA",
                            gabarito_fonte="oficial" if g_of else ("transcrito" if g_tr else None)))
        print(f"{nome}: {len(qs)} questões | gabarito {'oficial' if g_of else 'transcrito' if g_tr else 'NÃO ENCONTRADO'} "
              f"({len(gab or {})} itens) | 1ª específica: {n_esp} | conflitos oficial×transcrito: {conflito}")
    with open(os.path.join(BASE, "data", "historico_bruto.jsonl"), "w", encoding="utf-8") as f:
        for q in out:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print("total", len(out))

if __name__ == "__main__":
    main()
