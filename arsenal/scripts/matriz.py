"""Gera data/matriz.csv.

p_historico: (n_tema + 1) / (N_disciplina + K) — suavização de Laplace (prior uniforme
dentro da disciplina). Enquanto não houver histórico IGEDUC coletado (N = 0), p = 1/K.
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from taxonomia import DISCIPLINAS, TEMAS

BASE = os.path.join(os.path.dirname(__file__), "..")

def carregar_historico():
    path = os.path.join(BASE, "data", "historico.jsonl")
    cont = {}
    if os.path.exists(path):
        for linha in open(path, encoding="utf-8"):
            q = json.loads(linha)
            cont[(q["disciplina"], q["tema"])] = cont.get((q["disciplina"], q["tema"]), 0) + 1
    return cont

def carregar_acertos():
    path = os.path.join(BASE, "data", "acertos.json")
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}

def gerar():
    hist = carregar_historico()
    acertos = carregar_acertos()
    linhas = []
    for disc, temas in TEMAS.items():
        nq, peso, taxa0 = DISCIPLINAS[disc]
        n_disc = sum(v for (d, _), v in hist.items() if d == disc)
        k = len(temas)
        for tema in temas:
            n = hist.get((disc, tema), 0)
            p = (n + 1) / (n_disc + k)
            pts = p * nq * peso
            a = acertos.get(f"{disc}|{tema}", {})
            taxa = a["acertos"] / a["total"] if a.get("total", 0) >= 5 else taxa0
            linhas.append(dict(
                disciplina=disc, tema=tema, n_historico=n, N_disciplina=n_disc,
                p_historico=round(p, 4), peso_edital=peso,
                pontos_esperados=round(pts, 3),
                taxa_acerto_atual=round(taxa, 3),
                fonte_taxa="simulador" if a.get("total", 0) >= 5 else "estimativa inicial",
                dificuldade_para_mim=round(1 - taxa, 3),
                prioridade=round(pts * (1 - taxa), 3)))
    linhas.sort(key=lambda r: -r["prioridade"])
    out = os.path.join(BASE, "data", "matriz.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
        w.writeheader(); w.writerows(linhas)
    return linhas

if __name__ == "__main__":
    ls = gerar()
    print(f"matriz.csv: {len(ls)} temas")
    for r in ls[:10]:
        print(f"  {r['prioridade']:.3f}  {r['disciplina']:<14} {r['tema']}")
