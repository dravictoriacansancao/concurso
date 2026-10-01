"""Etapa 3: raio-X estatístico das provas reais IGEDUC (data/historico.jsonl) → relatorio/raio-x-dados.json + tabelas."""
import json, math, os, re, itertools
from collections import Counter, defaultdict
from difflib import SequenceMatcher
BASE = os.path.join(os.path.dirname(__file__), "..")
H = [json.loads(l) for l in open(os.path.join(BASE, "data", "historico.jsonl"), encoding="utf-8")]
V = [q for q in H if not q["anulada"]]

def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; d = 1 + z*z/n; c = (p + z*z/(2*n)) / d; m = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return (max(0, c - m), min(1, c + m))

def chi2_df3_p(x):  # sobrevivência da qui-quadrado com 3 g.l.
    phi = 0.5 * (1 + math.erf(math.sqrt(x) / math.sqrt(2)))
    return 2 * (1 - phi) + math.sqrt(2 * x / math.pi) * math.exp(-x / 2)

R = {}
# 1. frequência por disciplina/tema
R["por_disciplina"] = Counter(q["disciplina"] for q in H)
R["por_tema"] = Counter(f"{q['disciplina']} | {q['tema']}" for q in H)
# 2. letras
L = Counter(q["gabarito"] for q in V); n = len(V); exp = n / 4
chi = sum((L[l] - exp) ** 2 / exp for l in "ABCD")
R["letras"] = {"contagem": {l: L[l] for l in "ABCD"}, "n": n, "chi2": round(chi, 2), "p": round(chi2_df3_p(chi), 3)}
R["letras_por_prova"] = {}
for f in sorted({q["fonte"] for q in V}):
    c = Counter(q["gabarito"] for q in V if q["fonte"] == f); m = sum(c.values()); e = m / 4
    x = sum((c[l] - e) ** 2 / e for l in "ABCD")
    R["letras_por_prova"][f] = {"contagem": {l: c[l] for l in "ABCD"}, "n": m, "chi2": round(x, 2), "p": round(chi2_df3_p(x), 3)}
# 3. distratores
RESTR = ["exclusivamente", "apenas", "somente", "sempre", "nunca", "dispensa", "independentemente", "por si só",
         "restringe", "unicamente", "totalmente", "todos", "nenhum", "qualquer", "obrigatoriamente", "jamais", "único", "única",
         "suficiente", "garante", "elimina", "impede", "proíbe", "vedado", "somente"]
ADIT = [" e ", "além de", "bem como", "tanto", "considerando", "articul", "integr", "conjunt", "associad", "complementa"]
def tem(w, t): return re.search(r"(?<![\wÀ-ú])" + re.escape(w), t, re.I) is not None
pal = {}
for w in sorted(set(RESTR)):
    cc = sum(tem(w, q["alternativas"][q["gabarito"]]) for q in V)
    ce = sum(tem(w, t) for q in V for l, t in q["alternativas"].items() if l != q["gabarito"])
    nc, ne = len(V), 3 * len(V)
    if cc + ce >= 3:
        orr = ((cc + .5) / (nc - cc + .5)) / ((ce + .5) / (ne - ce + .5))
        pal[w] = {"na_correta": cc, "nas_erradas": ce, "pct_correta": round(cc / nc, 3), "pct_errada": round(ce / ne, 3), "odds_ratio": round(orr, 2)}
R["palavras_restritivas"] = dict(sorted(pal.items(), key=lambda x: x[1]["odds_ratio"]))
def score_abs(t): return sum(tem(w, t) for w in RESTR)
def score_int(t): return sum(t.lower().count(w) for w in ADIT) - 2 * score_abs(t)
# 4–5. comando e tipo
R["comando"] = Counter(q["comando"] for q in H)
R["tipo_por_disciplina"] = {d: dict(Counter(q["tipo_enunciado"] for q in H if q["disciplina"] == d)) for d in R["por_disciplina"]}
# 6. normas citadas no bloco SUS
R["normas_SUS"] = Counter(nm for q in H if q["disciplina"] == "SUS" for nm in q["norma_citada"])
# 7. repetição entre provas
rep = []
for a, b in itertools.combinations(H, 2):
    if a["concurso"] != b["concurso"]:
        s = SequenceMatcher(None, a["enunciado"], b["enunciado"]).ratio()
        if s > 0.8: rep.append((a["concurso"], a["numero"], b["concurso"], b["numero"], round(s, 2)))
R["repeticoes"] = rep
# 8. heurísticas de chute
def acc(nome, escolhe, grupo=None):
    qs = [q for q in V if grupo is None or grupo(q)]
    k = sum(escolhe(q) == q["gabarito"] for q in qs); lo, hi = wilson(k, len(qs))
    return {"heuristica": nome, "acertos": k, "n": len(qs), "taxa": round(k / len(qs), 3) if qs else None, "ic95": [round(lo, 3), round(hi, 3)]}
def mais_longa(q): return max(q["alternativas"], key=lambda l: (len(q["alternativas"][l]), l))
def mais_curta(q): return min(q["alternativas"], key=lambda l: (len(q["alternativas"][l]), l))
def menos_absoluta(q): return min(q["alternativas"], key=lambda l: (score_abs(q["alternativas"][l]), -len(q["alternativas"][l])))
def integradora(q): return max(q["alternativas"], key=lambda l: (score_int(q["alternativas"][l]), len(q["alternativas"][l])))
def elimina_abs_esperado(qs):
    tot = 0
    for q in qs:
        rest = [l for l, t in q["alternativas"].items() if score_abs(t) == 0] or list(q["alternativas"])
        tot += (1 / len(rest)) if q["gabarito"] in rest else 0
    return tot
grupos = {"todas": None, "Gerais (Port/Const/Inf)": lambda q: q["disciplina"] in ("Português", "Constitucional", "Informática"),
          "SUS + específicas de saúde": lambda q: q["disciplina"] in ("SUS", "Específica (outro cargo)"),
          "'mais correta e completa'": lambda q: "complet" in q["enunciado"].lower()}
R["heuristicas"] = []
for gn, g in grupos.items():
    for nome, f in [("alternativa mais longa", mais_longa), ("alternativa mais curta", mais_curta),
                    ("menos palavras absolutas (desempate: mais longa)", menos_absoluta), ("mais integradora", integradora)]:
        r = acc(nome, f, g); r["grupo"] = gn; R["heuristicas"].append(r)
    qs = [q for q in V if g is None or g(q)]
    e = elimina_abs_esperado(qs); lo, hi = wilson(round(e), len(qs))
    R["heuristicas"].append({"heuristica": "eliminar alternativas com absolutos e chutar entre as restantes", "grupo": gn,
                             "acertos": round(e, 1), "n": len(qs), "taxa": round(e / len(qs), 3), "ic95": [round(lo, 3), round(hi, 3)]})
# posição da correta no ranking de tamanho
pos = Counter()
for q in V:
    ordem = sorted(q["alternativas"], key=lambda l: -len(q["alternativas"][l])); pos[ordem.index(q["gabarito"])] += 1
R["posicao_tamanho_correta"] = {k: pos[k] for k in range(4)}
json.dump(R, open(os.path.join(BASE, "relatorio", "raio-x-dados.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=list)
print(json.dumps({k: R[k] for k in ("letras", "comando", "posicao_tamanho_correta", "repeticoes")}, ensure_ascii=False, default=list))
print("tipo:", R["tipo_por_disciplina"])
for h in R["heuristicas"]: print(f"  {h['grupo']:<26} {h['heuristica']:<58} {h['taxa']:.0%}  IC95 {h['ic95']}  n={h['n']}")
print("palavras:", json.dumps(R["palavras_restritivas"], ensure_ascii=False))
for f, v in R["letras_por_prova"].items(): print(f[:45], v)
