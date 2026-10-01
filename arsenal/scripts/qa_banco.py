"""Controle de qualidade do banco: formato, tamanho das alternativas, letras, duplicatas, fundamento."""
import json, os, sys
from collections import Counter
from difflib import SequenceMatcher
BASE = os.path.join(os.path.dirname(__file__), "..")
TOL = 0.25  # menor alternativa >= 75% da maior (exceto alternativas muito curtas)

def main():
    banco = [json.loads(l) for l in open(os.path.join(BASE, "data", "banco.jsonl"), encoding="utf-8")]
    erros, avisos = [], []
    for q in banco:
        alts = q["alternativas"]
        if sorted(alts) != list("ABCDE"): erros.append(f"{q['id']}: alternativas != A-E")
        if q["gabarito"] not in alts: erros.append(f"{q['id']}: gabarito inválido")
        if not q["fundamento"].strip(): erros.append(f"{q['id']}: sem fundamento")
        if len(set(alts.values())) < 5: erros.append(f"{q['id']}: alternativas repetidas")
        tam = [len(v) for v in alts.values()]
        if max(tam) >= 40 and min(tam) < (1 - TOL) * max(tam):
            avisos.append(f"{q['id']}: tamanhos {min(tam)}–{max(tam)} (> 25%)")
    # duplicatas
    for i in range(len(banco)):
        for j in range(i + 1, len(banco)):
            a, b = banco[i]["enunciado"], banco[j]["enunciado"]
            if SequenceMatcher(None, a, b).ratio() > 0.85:
                erros.append(f"duplicata provável: {banco[i]['id']} × {banco[j]['id']}")
    letras = Counter(q["gabarito"] for q in banco)
    n = len(banco)
    print(f"Questões: {n}")
    print("Por disciplina:", dict(Counter(q["disciplina"] for q in banco)))
    print("Letras:", {l: f"{letras[l]} ({letras[l]/n:.0%})" for l in "ABCDE"})
    fora = [l for l in "ABCDE" if not 0.18 <= letras[l] / n <= 0.22]
    if fora: avisos.append(f"letras fora de 18–22%: {fora}")
    cmd = Counter(q["comando"] for q in banco)
    print("Comando:", dict(cmd), f"→ INCORRETA {cmd.get('INCORRETA',0)/n:.0%}")
    tipo = Counter((q["disciplina"], q["tipo_enunciado"]) for q in banco)
    for d in ("SUS", "Perícia"):
        s, t = tipo.get((d, "situacional"), 0), sum(v for (dd, _), v in tipo.items() if dd == d)
        print(f"Situacionais {d}: {s}/{t} ({s/t:.0%})" if t else "")
    print("Marcadas verificar:", sum(q["verificar"] for q in banco))
    for e in erros: print("ERRO  ", e)
    for a in avisos: print("AVISO ", a)
    print("OK" if not erros else f"{len(erros)} erro(s)")
    return 1 if erros else 0

if __name__ == "__main__":
    sys.exit(main())
