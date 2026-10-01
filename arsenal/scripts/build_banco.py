"""Lê fonte/*.py, sorteia letras de forma balanceada e grava data/banco.jsonl."""
import importlib.util, json, os, random, sys, glob, csv
BASE = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(BASE, "fonte"))
sys.path.insert(0, os.path.dirname(__file__))
from taxonomia import TEMAS

PREFIXO = {"SUS": "SUS", "Perícia": "PER", "Constitucional": "CON", "Informática": "INF", "Português": "POR"}
LETRAS = "ABCDE"

def carregar_fontes():
    questoes, textos = [], {}
    for path in sorted(glob.glob(os.path.join(BASE, "fonte", "*.py"))):
        nome = os.path.basename(path)
        if nome.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(nome[:-3], path)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        questoes += mod.Q
        textos.update(getattr(mod, "TEXTOS", {}))
    # lotes gerados por scripts/gerar.py (JSON)
    for path in sorted(glob.glob(os.path.join(BASE, "fonte", "gerado_*.json"))):
        lote = json.load(open(path, encoding="utf-8"))
        for g in lote["questoes"]:
            questoes.append(dict(
                disciplina=g["disciplina"], tema=g["tema"], subtema=g["subtema"], dificuldade=g["dificuldade"],
                tipo_enunciado=g["tipo_enunciado"], comando=g["comando"], enunciado=g["enunciado"],
                correta=g["correta"], erradas=[(e["texto"], e["por_que"]) for e in g["erradas"]],
                comentario_correta=g["comentario_correta"], fundamento=g["fundamento"],
                pegadinha=g["pegadinha"], verificar=g.get("verificar", True), texto=None))
    return questoes, textos

def prob_tema():
    m = {}
    path = os.path.join(BASE, "data", "matriz.csv")
    for r in csv.DictReader(open(path, encoding="utf-8")):
        m[(r["disciplina"], r["tema"])] = float(r["p_historico"])
    return m

def main():
    questoes, textos = carregar_fontes()
    probs = prob_tema()
    rng = random.Random(20261101)
    # letras balanceadas: ciclo ABCDE embaralhado, por disciplina
    por_disc = {}
    for q in questoes:
        por_disc.setdefault(q["disciplina"], []).append(q)
    banco = []
    for disc, qs in por_disc.items():
        letras = [LETRAS[i % 5] for i in range(len(qs))]
        rng.shuffle(letras)
        for i, (q, letra) in enumerate(zip(qs, letras), 1):
            if q["tema"] not in TEMAS[disc]:
                raise SystemExit(f"Tema fora da taxonomia: {disc} / {q['tema']}")
            outras = [l for l in LETRAS if l != letra]
            erradas = q["erradas"][:]
            rng.shuffle(erradas)
            alts, porque = {letra: q["correta"]}, {letra: "Esta é a alternativa a ser marcada."}
            for l, (txt, why) in zip(outras, erradas):
                alts[l], porque[l] = txt, why
            banco.append(dict(
                id=f"{PREFIXO[disc]}-{i:03d}", disciplina=disc, tema=q["tema"], subtema=q["subtema"],
                dificuldade=q["dificuldade"], tipo_enunciado=q["tipo_enunciado"], comando=q["comando"],
                texto=q["texto"], enunciado=q["enunciado"],
                alternativas={l: alts[l] for l in LETRAS}, gabarito=letra,
                comentario_correta=q["comentario_correta"],
                por_que_cada_errada={l: porque[l] for l in LETRAS},
                fundamento=q["fundamento"], pegadinha=q["pegadinha"],
                prob_tema=probs.get((disc, q["tema"]), 0.0), verificar=q["verificar"]))
    with open(os.path.join(BASE, "data", "banco.jsonl"), "w", encoding="utf-8") as f:
        for q in banco:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    with open(os.path.join(BASE, "data", "textos.json"), "w", encoding="utf-8") as f:
        json.dump(textos, f, ensure_ascii=False, indent=1)
    print(f"banco.jsonl: {len(banco)} questões")

if __name__ == "__main__":
    main()
