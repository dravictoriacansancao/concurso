"""Gabaritos das provas de MÉDICO PERITO de outras bancas (data/raw_outras/). Um leitor por layout."""
import os, re, subprocess
RAW = os.path.join(os.path.dirname(__file__), "..", "data", "raw_outras")
def txt(nome, layout=True):
    a = ["pdftotext"] + (["-layout"] if layout else []) + [os.path.join(RAW, nome), "-"]
    return subprocess.run(a, capture_output=True, text=True).stdout
def norm(v):
    v = v.strip().upper()
    return "ANULADA" if v in ("X", "*", "NULA", "ANULADA") else v

def cebraspe(parte):
    t = txt(f"CEBRASPE_MPS-Perito-Medico-Federal-BR-2025_GABARITO_{parte}.pdf")
    g, itens = {}, None
    for l in t.split("\n"):
        if l.strip().startswith("Item"): itens = [int(x) for x in re.findall(r"\b\d+\b", l.strip()[4:])]
        elif l.strip().startswith("Gabarito") and itens:
            vals = l.split()[1:]
            g.update({n: norm(v) for n, v in zip(itens, vals) if n > 0}); itens = None
    return g

def linhas_pareadas(t, inicio_regex, fim_regex=None):
    """Blocos 'linha de números' seguida de 'linha de letras' (URCA, FGV, UFG)."""
    i = re.search(inicio_regex, t).end(); t = t[i:]
    if fim_regex:
        m = re.search(fim_regex, t); t = t[:m.start()] if m else t
    g, nums = {}, None
    for l in t.split("\n"):
        toks = l.split()
        if toks and all(x.isdigit() for x in toks): nums = [int(x) for x in toks]
        elif nums and toks:
            vals = [x for x in toks if re.fullmatch(r"[A-Ea-ex*]|Nula", x)]
            if len(vals) == len(nums): g.update({n: norm(v) for n, v in zip(nums, vals)})
            nums = None
    return g

def urca():
    t = txt("CEV-URCA_Varzea-Alegre-CE-2024_GABARITO.pdf")
    # o bloco do cargo traz 26–55; 1–25 (comuns) vêm no bloco imediatamente anterior
    # 01–25 vêm no bloco comum do NÍVEL SUPERIOR; 26–55 no bloco do cargo
    sup = t.index("NÍVEL SUPERIOR")
    j = t.index("MÉDICO PERITO")
    g = {k: v for k, v in linhas_pareadas(t[sup:j], r"PORTUGUÊS").items() if k <= 25}
    g.update(linhas_pareadas(t[j:], r"MÉDICO PERITO", r"Rua Cel"))
    return g

def fgv():
    return linhas_pareadas(txt("FGV_Macae-RJ-2024_GABARITO.pdf"), r"Médico Perito - TIPO 1\s*\n", r"\(\*\)")

def ufg():
    t = txt("UFG_Goiania-GO-2022_GABARITO.pdf")
    i = [m.start() for m in re.finditer(r"MÉDICO PERITO\s*\n\s*\n\s*01\s", t)][-1]
    return linhas_pareadas(t[i:], r"MÉDICO PERITO\s*\n", r"Questão Anulada")

def olinda():
    t = txt("UPENET-IAUPE_Olinda-PE-2024_GABARITO.pdf")
    return {int(n): norm(v) for n, v in re.findall(r"\b(\d{2})\s+([A-E]|X|\*)\b", t)}

def fundatec():
    t = txt("FUNDATEC_Nova-Santa-Rita-RS-2023_GABARITO.pdf")
    blocos = [m.start() for m in re.finditer(r"Cargo: 12 - Médico Perito Psiquiatra", t)]
    defin = [b for b in blocos if "Definitiv" in t[max(0, b - 400):b + 400]] or blocos
    b = defin[-1]; seg = t[b:b + 6000]
    g = {}
    for n, v in re.findall(r"^\s*(\d{1,2})\s+([A-E]|\*|Anulada)\s", seg, re.M):
        if int(n) not in g: g[int(n)] = norm(v)
    return g, ("definitivo" if defin != blocos or "Definitiv" in t[max(0, b - 400):b + 400] else "preliminar")

def unifil():
    t = txt("INSTITUTO-UNIFIL_Paranagua-PR-2022_GABARITO.pdf")
    i = t.index("ENFERMEIRO DO TRABALHO             MÉDICO PERITO") if "ENFERMEIRO DO TRABALHO             MÉDICO PERITO" in t else t.index("MÉDICO PERITO")
    g = {}
    for l in t[i:].split("\n")[1:25]:
        m = re.findall(r"(\d{1,2})\s+(Alterado\s+[A-D]|Anulad[ao]|[A-D])", l)
        if len(m) >= 4:
            for n, v in m[2:4]: g[int(n)] = norm(v.split()[-1]) if v.startswith("Alterado") else norm(v)
    return g

if __name__ == "__main__":
    for nome, f in [("CEBRASPE gerais", lambda: cebraspe("ConhecGerais")), ("CEBRASPE específicos", lambda: cebraspe("ConhecEspecificos")),
                    ("URCA", urca), ("FGV", fgv), ("UFG", ufg), ("OLINDA", olinda), ("FUNDATEC", fundatec), ("UNIFIL", unifil)]:
        g = f()
        if isinstance(g, tuple): g, tipo = g; nome += f" ({tipo})"
        ks = sorted(g); print(f"{nome:<22} {len(g):>3} itens  {ks[:1]}..{ks[-1:]}  anuladas={[k for k in ks if g[k]=='ANULADA']}  ex={[g[k] for k in ks[:8]]}")
