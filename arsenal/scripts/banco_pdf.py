"""Gera simulador/banco.pdf: todas as questões e, ao final, o gabarito comentado."""
import json, os
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
BASE = os.path.join(os.path.dirname(__file__), "..")
banco = [json.loads(l) for l in open(os.path.join(BASE, "data", "banco.jsonl"), encoding="utf-8")]
textos = json.load(open(os.path.join(BASE, "data", "textos.json"), encoding="utf-8"))
ss = getSampleStyleSheet()
H = ParagraphStyle("h", parent=ss["Heading2"], spaceBefore=10)
N = ParagraphStyle("n", parent=ss["BodyText"], fontSize=9.5, leading=13)
A = ParagraphStyle("a", parent=N, leftIndent=14)
P = ParagraphStyle("p", parent=N, fontSize=8.5, textColor="#444444")
e = lambda s: escape(s).replace("\n", "<br/>")
story = [Paragraph("Arsenal IGEDUC · Médico Perito Clínico Geral – Porto Calvo/AL", ss["Title"]),
         Paragraph(f"{len(banco)} questões inéditas. Gabarito comentado ao final.", N)]
ordem = ["Português", "Constitucional", "Informática", "Perícia", "SUS"]
num, vistos = 0, set()
for d in ordem:
    story.append(Paragraph(d, H))
    for q in [q for q in banco if q["disciplina"] == d]:
        num += 1; q["_n"] = num
        if q["texto"] and q["texto"] not in vistos:
            vistos.add(q["texto"]); story.append(Paragraph(e(textos[q["texto"]]), P)); story.append(Spacer(1, 6))
        story.append(Paragraph(f"<b>{num}.</b> ({q['id']} · {e(q['tema'])}) {e(q['enunciado'])}", N))
        for L in "ABCDE":
            story.append(Paragraph(f"({L}) {e(q['alternativas'][L])}", A))
        story.append(Spacer(1, 8))
story += [PageBreak(), Paragraph("Gabarito comentado", ss["Heading1"])]
for d in ordem:
    for q in [q for q in banco if q["disciplina"] == d]:
        story.append(Paragraph(f"<b>{q['_n']}. {q['gabarito']}</b> — {e(q['comentario_correta'])} <i>({e(q['fundamento'])})</i> Pegadinha: {e(q['pegadinha'])}", N))
        story.append(Spacer(1, 4))
SimpleDocTemplate(os.path.join(BASE, "simulador", "banco.pdf"), pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                  topMargin=1.8*cm, bottomMargin=1.8*cm, title="Arsenal IGEDUC – banco de questões").build(story)
print(f"banco.pdf: {len(banco)} questões")
