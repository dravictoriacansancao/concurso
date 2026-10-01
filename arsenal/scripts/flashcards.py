"""Gera simulador/flashcards.csv (frente;verso) para importar no Anki."""
import json, os
BASE = os.path.join(os.path.dirname(__file__), "..")
def limpa(s): return s.replace(";", ",").replace("\n", " ").strip()
banco = [json.loads(l) for l in open(os.path.join(BASE, "data", "banco.jsonl"), encoding="utf-8")]
n = 0
with open(os.path.join(BASE, "simulador", "flashcards.csv"), "w", encoding="utf-8") as f:
    for q in banco:
        if q["disciplina"] == "Português":
            continue
        frente = f"[{q['disciplina']} · {q['tema']}] {q['subtema']}"
        verso = f"{q['comentario_correta']} — {q['fundamento']}"
        f.write(f"{limpa(frente)};{limpa(verso)}\n"); n += 1
print(f"flashcards.csv: {n} cartões")
