"""Embute banco + textos + matriz no simulador.

Gera:
  simulador/index.html  – arquivo completo para abrir offline (dois cliques)
  simulador/web.html    – mesma página sem o esqueleto <html>, para publicar como Artifact
"""
import csv, json, os
BASE = os.path.join(os.path.dirname(__file__), "..")

def main():
    banco = [json.loads(l) for l in open(os.path.join(BASE, "data", "banco.jsonl"), encoding="utf-8")]
    textos = json.load(open(os.path.join(BASE, "data", "textos.json"), encoding="utf-8"))
    matriz = []
    for r in csv.DictReader(open(os.path.join(BASE, "data", "matriz.csv"), encoding="utf-8")):
        matriz.append({"disciplina": r["disciplina"], "tema": r["tema"], "p_historico": float(r["p_historico"])})
    reais = []
    hp = os.path.join(BASE, "data", "historico.jsonl")
    if os.path.exists(hp):
        for l in open(hp, encoding="utf-8"):
            h = json.loads(l)
            if h["anulada"]:
                continue
            reais.append({"id": f"R{h['concurso']}-{h['numero']:02d}", "real": True,
                          "origem": f"{h['municipio']}/{h['uf']} {h['ano']} · {h['cargo'].title()} · {'item' if h['formato'] == 'V/F' else 'questão'} {h['numero']}" + (" · gabarito preliminar" if h.get('preliminar') else ""),
                          "disciplina": h["disciplina"], "tema": h["tema"], "subtema": h["tema"], "dificuldade": 0,
                          "comando": "CORRETA" if h["formato"] == "V/F" else h["comando"], "texto": None,
                          "enunciado": ("Julgue o item: " if h["formato"] == "V/F" else "") + h["enunciado"],
                          "alternativas": h["alternativas"], "gabarito": h["gabarito"], "verificar": False})
    data = json.dumps({"banco": banco, "reais": reais, "textos": textos, "matriz": matriz}, ensure_ascii=False).replace("</", "<\\/")
    tpl = open(os.path.join(BASE, "simulador", "template.html"), encoding="utf-8").read()
    page = tpl.replace("/*__DATA__*/", data)
    open(os.path.join(BASE, "simulador", "web.html"), "w", encoding="utf-8").write(page)
    full = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
    open(os.path.join(BASE, "simulador", "index.html"), "w", encoding="utf-8").write(full)
    print(f"simulador: {len(banco)} inéditas + {len(reais)} reais, {len(full)//1024} KB")

if __name__ == "__main__":
    main()
