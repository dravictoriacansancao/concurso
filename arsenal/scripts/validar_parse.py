"""Confere se cada questão do histórico tem alternativas completas e gabarito válido."""
import json, os, sys
from collections import Counter
BASE = os.path.join(os.path.dirname(__file__), "..")
path = os.path.join(BASE, "data", sys.argv[1] if len(sys.argv) > 1 else "historico.jsonl")
hist = [json.loads(l) for l in open(path, encoding="utf-8")]
erros = []
for q in hist:
    n = len(q["alternativas"]); letras = "".join(sorted(q["alternativas"]))
    if letras not in ("ABCD", "ABCDE", "FV"): erros.append(f"{q['fonte'][:40]} Q{q['numero']}: alternativas {letras}")
    if not q["anulada"] and q["gabarito"] not in q["alternativas"]: erros.append(f"{q['fonte'][:40]} Q{q['numero']}: gabarito {q['gabarito']}")
    if len(q["enunciado"]) < 15: erros.append(f"{q['fonte'][:40]} Q{q['numero']}: enunciado curto")
print(f"{len(hist)} questões · nº de alternativas: {dict(Counter(len(q['alternativas']) for q in hist))} · anuladas: {sum(q['anulada'] for q in hist)}")
for e in erros: print("ERRO", e)
print("OK" if not erros else f"{len(erros)} erro(s)")
