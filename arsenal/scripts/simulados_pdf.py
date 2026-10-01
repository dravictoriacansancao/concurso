"""Gera 3 simulados no formato da prova de Porto Calvo (50 questões A–E, distribuição do edital),
sem repetir questão entre eles, com folha de respostas e gabarito comentado no final.

Saída: simulados/simulado-{1,2,3}.html e .pdf (PDF via Chromium headless).
Fontes: inéditas (data/banco.jsonl) + provas reais IGEDUC A–E (data/historico.jsonl)
+ provas de perito de outras bancas A–E (data/outras.jsonl).
"""
import html, json, os, random, re, subprocess

BASE = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(BASE, "simulados")
load = lambda p: [json.loads(l) for l in open(os.path.join(BASE, "data", p), encoding="utf-8")]
banco, hist, outras = load("banco.jsonl"), load("historico.jsonl"), load("outras.jsonl")
textos = json.load(open(os.path.join(BASE, "data", "textos.json"), encoding="utf-8"))
TITULO_TEXTO = {k: v.split("\n", 1)[0] for k, v in textos.items()}

ORDEM = [("Português", 10, 1.1), ("Constitucional", 5, 1.1), ("Informática", 5, 1.1),
         ("Perícia", 15, 2.6), ("SUS", 15, 2.6)]
NOME = {"Português": "Língua Portuguesa", "Constitucional": "Direito Constitucional", "Informática": "Informática",
        "Perícia": "Conhecimentos Profissionais", "SUS": "Legislação, Políticas e Gestão do SUS"}

# Itens reais revisados à mão: autocontidos (trazem o trecho), sem defeito de extração e no tema certo.
REAIS_PORT = [233, 236, 237, 238, 239, 240, 241, 286, 287, 290, 435, 436, 437, 438, 439, 441, 442,
              549, 550, 551, 552, 553, 554, 555]
REAIS_CONST = [557, 558, 559, 560, 652, 654, 655, 656]
REAIS_INFO = [248, 249, 250, 251, 252, 657, 658, 659, 661]
REAIS_PER = [325, 669]
REAIS_SUS_EXTRA = [274]  # classificado como Constitucional, mas é Lei 8.142


def limpa(s):
    s = re.sub(r"\s+(?:[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}[ ,]*){2,}$", "", s.strip())  # título de seção grudado no fim
    return s.replace("? órgão é", " órgão é?").replace("qual responsável", "qual")


def real(i, d):
    q = hist[i]
    return {"disc": d, "enun": limpa(q["enunciado"]), "alt": {k: limpa(v) for k, v in q["alternativas"].items()},
            "gab": q["gabarito"], "origem": f"IGEDUC · {q['municipio']}/{q['uf']} {q['ano']} (prova real)",
            "tema": q.get("tema", ""), "coment": "", "texto": None}


def inedita(q):
    c = q["comentario_correta"]
    if q.get("pegadinha"):
        c += f" <b>Pegadinha:</b> {html.escape(q['pegadinha'])}"
    return {"disc": q["disciplina"], "enun": q["enunciado"], "alt": q["alternativas"], "gab": q["gabarito"],
            "origem": f"Inédita {q['id']}", "tema": q["tema"], "coment": c, "fund": q.get("fundamento", ""),
            "texto": q["texto"]}


def outra(q):
    return {"disc": q["disciplina"], "enun": limpa(q["enunciado"]),
            "alt": {k: limpa(v) for k, v in q["alternativas"].items()}, "gab": q["gabarito"],
            "origem": f"{q['banca']} · {q['municipio']}/{q['uf']} {q['ano']} ({q['cargo']})",
            "tema": q.get("tema", ""), "coment": "", "texto": None}


rnd = random.Random(20261101)


def reparte(lst, n_por_prova):
    lst = lst[:]; rnd.shuffle(lst)
    return [lst[i * n_por_prova:(i + 1) * n_por_prova] for i in range(3)]


B = lambda d: [inedita(q) for q in banco if q["disciplina"] == d]
O = lambda d: [outra(q) for q in outras if q["disciplina"] == d and q["formato"] == "A-E" and not q["anulada"]]

# SUS real: A–E, sem repetição entre cadernos do mesmo concurso, sem itens que dependem de estatuto local.
vistos, sus_reais = set(), []
for i, q in enumerate(hist):
    if q["disciplina"] == "SUS" and q["formato"] == "5 alternativas" and not q["anulada"]:
        k = q["enunciado"][:90]
        if k in vistos or re.search(r"Consórcio|Estatuto|o texto", q["enunciado"]):
            continue
        vistos.add(k); sus_reais.append(real(i, "SUS"))
sus_reais += [real(i, "SUS") for i in REAIS_SUS_EXTRA]

# Português: cada prova recebe um bloco de texto inédito ou as avulsas, + itens reais.
port_ined = B("Português")
blocos = [[q for q in port_ined if q["texto"] == "T1"], [q for q in port_ined if q["texto"] == "T2"],
          [q for q in port_ined if not q["texto"]]]
port_reais = reparte([real(i, "Português") for i in REAIS_PORT], 8)

const_i, const_r, const_o = reparte(B("Constitucional"), 2), reparte([real(i, "Constitucional") for i in REAIS_CONST], 2), reparte(O("Constitucional"), 2)
info_i, info_r = reparte(B("Informática"), 2), reparte([real(i, "Informática") for i in REAIS_INFO], 3)
per_i = reparte(B("Perícia"), 8)
per_o = reparte(O("Perícia") + [real(i, "Perícia") for i in REAIS_PER], 7)
sus_i, sus_r, sus_o = reparte(B("SUS"), 6), reparte(sus_reais, 7), reparte(O("SUS"), 2)

provas = []
for p in range(3):
    port = blocos[p] + port_reais[p][:10 - len(blocos[p])]
    const = (const_i[p] + const_r[p] + const_o[p])[:5]
    info = info_i[p] + info_r[p]
    per = per_i[p] + per_o[p]
    sus = sus_i[p] + sus_r[p] + sus_o[p]
    for grupo in (const, info, per, sus):
        rnd.shuffle(grupo)
    texto_primeiro = sorted(port, key=lambda q: q["texto"] is None)  # bloco do texto abre a prova
    provas.append(texto_primeiro + const + info + per + sus)

for p, prova in enumerate(provas):
    assert [q["disc"] for q in prova] == sum([[d] * n for d, n, _ in ORDEM], []), p
    for q in prova:
        assert sorted(q["alt"]) == list("ABCDE") and q["gab"] in "ABCDE", q["origem"]
chaves = [q["enun"][:80] for pr in provas for q in pr]
assert len(chaves) == len(set(chaves)), "questão repetida entre simulados"

e = lambda s: html.escape(s).replace("\n", "<br>")
CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body { font-family: 'Georgia', 'Times New Roman', serif; font-size: 10.3pt; line-height: 1.42; color: #111; margin: 0; }
h1 { font-size: 17pt; margin: 0 0 2mm; }
h2 { font-size: 12pt; margin: 6mm 0 3mm; padding: 1.5mm 3mm; background: #1f3a5f; color: #fff; letter-spacing: .3px;
     break-after: avoid; }
.capa { border: 1.5px solid #1f3a5f; padding: 7mm; margin-bottom: 6mm; }
.capa p { margin: 1.5mm 0; }
.sub { color: #444; font-size: 10pt; }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; }
th, td { border: 1px solid #999; padding: 1.4mm 2mm; text-align: left; vertical-align: top; }
th { background: #e8edf3; }
.q { break-inside: avoid; margin: 0 0 4.5mm; }
.q .n { font-weight: bold; }
.alt { margin: 1mm 0 0 6mm; text-indent: -6mm; padding-left: 6mm; }
.texto { border-left: 3px solid #1f3a5f; padding: 2mm 4mm; margin: 0 0 5mm; background: #f6f8fb; font-size: 9.8pt; }
.texto b { display: block; margin-bottom: 1.5mm; }
.quebra { break-before: page; }
.folha td, .folha th { text-align: center; padding: 1.2mm; }
.bol { display: inline-block; width: 5.2mm; height: 5.2mm; border: 1px solid #555; border-radius: 50%; font-size: 7.5pt;
       line-height: 5mm; text-align: center; margin: 0 .6mm; }
.gab td { font-size: 9pt; }
.gab .L { font-weight: bold; font-size: 11pt; text-align: center; width: 9mm; }
.origem { color: #555; font-size: 8.5pt; }
.dica { font-size: 9.3pt; background: #fff7e0; border: 1px solid #e3c766; padding: 3mm 4mm; margin-top: 4mm; }
"""


def render(p, prova):
    n = p + 1
    out = [f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Simulado {n} – Médico Perito Porto Calvo</title>"
           f"<style>{CSS}</style></head><body>"]
    out.append(f"""<div class='capa'><h1>SIMULADO {n} · Médico Perito Clínico Geral</h1>
<p class='sub'>Prefeitura de Porto Calvo/AL · Edital nº 001/2026 · modelo Instituto IGEDUC</p>
<p><b>50 questões · 5 alternativas (A–E) · 4 horas</b> (prova real: domingo, 01/11/2026, 14h às 18h).</p>
<table><tr><th>Disciplina</th><th>Questões</th><th>Pontos/questão</th><th>Total</th></tr>
<tr><td>Língua Portuguesa</td><td>01–10</td><td>1,1</td><td>11</td></tr>
<tr><td>Direito Constitucional</td><td>11–15</td><td>1,1</td><td>5,5</td></tr>
<tr><td>Informática</td><td>16–20</td><td>1,1</td><td>5,5</td></tr>
<tr><td>Conhecimentos Profissionais (perícia)</td><td>21–35</td><td>2,6</td><td>39</td></tr>
<tr><td>Legislação, Políticas e Gestão do SUS</td><td>36–50</td><td>2,6</td><td>39</td></tr>
<tr><th>Total</th><th>50</th><th></th><th>100</th></tr></table>
<p class='dica'>Para valer como treino: cronometre 4 h, marque na <b>folha de respostas</b> (penúltima parte) e só depois
abra o <b>gabarito</b> no final. Eliminação na prova real: menos de <b>70 pontos</b> ou <b>zero</b> em qualquer disciplina.
Questões marcadas “prova real” são da própria IGEDUC ou de concursos de perito de outras bancas; “inédita” foi escrita
no estilo da banca e traz comentário no gabarito.</p></div>""")
    atual, textos_feitos = None, set()
    for i, q in enumerate(prova, 1):
        if q["disc"] != atual:
            atual = q["disc"]
            out.append(f"<h2>{NOME[atual].upper()}</h2>")
        if q["texto"] and q["texto"] not in textos_feitos:
            textos_feitos.add(q["texto"])
            ini = [j for j, x in enumerate(prova, 1) if x["texto"] == q["texto"]]
            corpo = textos[q["texto"]].split("\n", 1)
            out.append(f"<div class='texto'><i>Leia o texto a seguir para responder às questões {ini[0]:02d} a {ini[-1]:02d}.</i>"
                       f"<b>{e(corpo[0])}</b>{e(corpo[1].strip())}</div>")
        alts = "".join(f"<div class='alt'>({L}) {e(q['alt'][L])}</div>" for L in "ABCDE")
        out.append(f"<div class='q'><span class='n'>QUESTÃO {i:02d}</span> — {e(q['enun'])}{alts}</div>")

    # Folha de respostas
    out.append("<div class='quebra'></div><h2>FOLHA DE RESPOSTAS</h2><table class='folha'><tr>")
    for col in range(2):
        out.append("<td style='border:none;padding:0 2mm'><table>")
        for i in range(col * 25 + 1, col * 25 + 26):
            bol = "".join(f"<span class='bol'>{L}</span>" for L in "ABCDE")
            out.append(f"<tr><th>{i:02d}</th><td>{bol}</td></tr>")
        out.append("</table></td>")
    out.append("</tr></table>")
    out.append("""<p class='sub'>Início: ____:____ · Término: ____:____</p>""")

    # Gabarito
    out.append(f"<div class='quebra'></div><h2>GABARITO · SIMULADO {n}</h2>")
    linhas = ""
    for blk in range(0, 50, 10):
        linhas += "<tr>" + "".join(f"<th>{i + 1:02d}</th>" for i in range(blk, blk + 10)) + "</tr>"
        linhas += "<tr>" + "".join(f"<td style='text-align:center;font-weight:bold'>{prova[i]['gab']}</td>" for i in range(blk, blk + 10)) + "</tr>"
    out.append(f"<table class='folha'>{linhas}</table>")
    out.append("""<h2>CÁLCULO DA NOTA</h2><table><tr><th>Disciplina</th><th>Acertos</th><th>× peso</th><th>Pontos</th></tr>
<tr><td>Português (01–10)</td><td>___ /10</td><td>× 1,1</td><td>____</td></tr>
<tr><td>Constitucional (11–15)</td><td>___ /5</td><td>× 1,1</td><td>____</td></tr>
<tr><td>Informática (16–20)</td><td>___ /5</td><td>× 1,1</td><td>____</td></tr>
<tr><td>Conhecimentos Profissionais (21–35)</td><td>___ /15</td><td>× 2,6</td><td>____</td></tr>
<tr><td>SUS (36–50)</td><td>___ /15</td><td>× 2,6</td><td>____</td></tr>
<tr><th colspan='3'>TOTAL (mínimo 70, sem zerar nenhuma)</th><th>____ /100</th></tr></table>
<p class='sub'>Referência: com 10 acertos em perícia e 10 em SUS você já soma 52 pontos; os outros 18 saem das gerais
(ex.: 7 de Português + 3 de Constitucional + 3 de Informática = 14,3 → total 66,3. Ou seja: 11/15 em cada específica
deixa a prova bem mais folgada).</p>""")
    out.append("<h2>GABARITO COMENTADO</h2><table class='gab'><tr><th>Q</th><th>Resp.</th><th>Tema · origem · comentário</th></tr>")
    for i, q in enumerate(prova, 1):
        com = q["coment"] if q["coment"] else ""
        if q["coment"]:
            com = html.escape(q["coment"].split(" <b>Pegadinha:</b> ")[0])
            if " <b>Pegadinha:</b> " in q["coment"]:
                com += " <b>Pegadinha:</b> " + q["coment"].split(" <b>Pegadinha:</b> ")[1]
            if q.get("fund"):
                com += f" <i>({html.escape(q['fund'])})</i>"
        else:
            com = "Gabarito oficial definitivo da banca."
        out.append(f"<tr><td>{i:02d}</td><td class='L'>{q['gab']}</td><td><b>{e(q['tema'])}</b> "
                   f"<span class='origem'>· {e(q['origem'])}</span><br>{com}</td></tr>")
    out.append("</table></body></html>")
    return "".join(out)


os.makedirs(OUT, exist_ok=True)
chrome = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
for p, prova in enumerate(provas):
    h = os.path.join(OUT, f"simulado-{p + 1}.html")
    open(h, "w", encoding="utf-8").write(render(p, prova))
    if os.path.exists(chrome):
        subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={h[:-5]}.pdf", "file://" + os.path.abspath(h)],
                       check=True, capture_output=True)
    from collections import Counter
    print(f"Simulado {p + 1}: gabarito {dict(sorted(Counter(q['gab'] for q in prova).items()))} · "
          f"origens {dict(Counter(q['origem'].split(' ')[0] for q in prova))}")
