"""Atualiza a matriz de prioridade com o progresso exportado do simulador.

Uso: python scripts/atualizar_matriz.py progresso.json
(No simulador: aba Progresso → Copiar progresso → cole num arquivo progresso.json)
"""
import json, os, subprocess, sys
BASE = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.dirname(__file__))
import matriz

def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    prog = json.load(open(sys.argv[1], encoding="utf-8"))
    banco = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(BASE, "data", "banco.jsonl"), encoding="utf-8")}
    acertos = {}
    for qid, resps in prog.get("resp", {}).items():
        q = banco.get(qid)
        if not q:
            continue
        k = f"{q['disciplina']}|{q['tema']}"
        a = acertos.setdefault(k, {"acertos": 0, "total": 0})
        for r in resps:
            a["total"] += 1; a["acertos"] += 1 if r["ok"] else 0
    json.dump(acertos, open(os.path.join(BASE, "data", "acertos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    linhas = matriz.gerar()
    for script in ("build_banco.py", "build_simulador.py"):
        subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), script)], check=True)
    print("Top 10 prioridades agora:")
    for r in linhas[:10]:
        print(f"  {r['prioridade']:.3f}  {r['disciplina']:<14} {r['tema']}  (acerto {r['taxa_acerto_atual']:.0%}, {r['fonte_taxa']})")

if __name__ == "__main__":
    main()
