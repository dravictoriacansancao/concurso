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
    data = json.dumps({"banco": banco, "textos": textos, "matriz": matriz}, ensure_ascii=False).replace("</", "<\\/")
    tpl = open(os.path.join(BASE, "simulador", "template.html"), encoding="utf-8").read()
    page = tpl.replace("/*__DATA__*/", data)
    open(os.path.join(BASE, "simulador", "web.html"), "w", encoding="utf-8").write(page)
    full = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
    open(os.path.join(BASE, "simulador", "index.html"), "w", encoding="utf-8").write(full)
    print(f"simulador: {len(banco)} questões, {len(full)//1024} KB")

if __name__ == "__main__":
    main()
