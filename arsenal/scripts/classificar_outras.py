"""Classifica as provas de perito de outras bancas (data/outras_bruto.jsonl) nos temas do SEU edital.
Revisão manual item a item. Ficam de fora: Português com texto-base (o texto não vem junto), conhecimentos
locais/atualidades, matemática, legislação municipal e de servidor, ética do servidor (não estão no edital).
Saída: data/outras.jsonl"""
import json, os, re
BASE = os.path.join(os.path.dirname(__file__), "..")

P, S, C, I, PT = "Perícia", "SUS", "Constitucional", "Informática", "Português"
CAP = (P, "Avaliação da capacidade laborativa"); NEXO = (P, "Avaliação de dano corporal e nexo causal")
INV = (P, "Avaliação de invalidez e incapacidade permanente"); CV = (P, "Avaliação pericial em doenças cardiovasculares")
DERM = (P, "Avaliação pericial em doenças dermatológicas"); END = (P, "Avaliação pericial em doenças endócrinas e metabólicas")
INF = (P, "Avaliação pericial em doenças infecciosas"); NEU = (P, "Avaliação pericial em doenças neurológicas")
OST = (P, "Avaliação pericial em doenças osteomusculares"); PSI = (P, "Avaliação pericial em doenças psiquiátricas")
RESP = (P, "Avaliação pericial em doenças respiratórias"); BIO = (P, "Bioética aplicada à perícia médica")
DD = (P, "Diagnóstico diferencial em clínica médica"); OCUP = (P, "Doenças ocupacionais e relacionadas ao trabalho")
EPI = (P, "Epidemiologia clínica aplicada à perícia"); EXAME = (P, "Exame clínico direcionado à perícia médica")
TEMP = (P, "Incapacidade temporária / permanente"); EXC = (P, "Interpretação de exames complementares")
PREV = (P, "Perícia médica previdenciária")
APS = (S, "APS e ESF"); CF196 = (S, "CF/88 arts. 196 a 200"); CS = (S, "Controle social"); FIN = (S, "Financiamento")
GEST = (S, "Gestão municipal do SUS"); IND = (S, "Indicadores e monitoramento"); L8080 = (S, "Lei nº 8.080/1990"); L8142 = (S, "Lei nº 8.142/1990")
DGF = (C, "Direitos e garantias fundamentais"); ADM = (C, "Administração Pública na CF"); POD = (C, "Organização dos Poderes")
PL = (C, "Processo legislativo"); DPOL = (C, "Direitos políticos"); RESPE = (C, "Responsabilidade do Estado")
FED = (C, "Federalismo e organização do Estado")
LGPD = (I, "Conceitos de segurança da informação e proteção de dados"); RED = (PT, "Redação Oficial")

def faixa(d, ini, fim, v):
    for n in range(ini, fim + 1): d[n] = v

M = {}
d = M["CEV-URCA"] = {26: L8080, 27: L8142, 28: CAP, 29: OCUP, 30: CV, 31: OCUP, 32: L8080, 33: PSI, 34: INV, 35: L8080,
     36: OCUP, 37: PREV, 38: OST, 39: OST, 40: END, 41: OCUP, 42: OCUP, 43: RESP, 44: CV, 45: NEU, 46: RESP, 47: BIO,
     48: IND, 49: PREV, 50: BIO, 51: BIO, 52: EPI, 53: OCUP, 54: L8080, 55: OST}
M["FGV"] = {31: L8080, 32: L8080, 33: L8080, 34: L8142, 35: GEST, 36: GEST, 37: GEST, 38: GEST, 39: GEST, 40: GEST,
     41: CV, 42: OCUP, 43: INF, 44: INF, 45: EPI, 46: PSI, 47: OCUP, 48: OST, 49: OCUP, 50: PSI, 51: EPI, 52: EPI,
     53: IND, 54: PREV, 55: OCUP, 56: IND, 57: END, 58: OCUP, 59: OCUP, 60: BIO, 61: OCUP, 62: OCUP, 63: OCUP, 64: OCUP,
     65: OCUP, 66: OCUP, 67: OCUP, 68: PREV, 69: NEXO, 70: OCUP}
M["FUNDATEC"] = {19: DGF, 20: DGF, 21: FED, 22: ADM, 23: POD, 24: PL, 26: DPOL, 27: DPOL, 29: PSI, 30: PSI, 31: PSI,
     32: PSI, 33: PSI, 34: PSI, 35: PSI, 36: PSI, 37: PSI, 38: EXAME, 39: PSI, 40: PSI}
d = M["Instituto UniFil"] = {11: L8080, 12: L8080, 13: L8080, 14: L8080, 15: FIN, 16: L8142, 17: APS, 18: GEST, 19: GEST,
     20: GEST, 21: BIO, 22: BIO, 23: PSI, 24: PSI, 25: NEXO, 26: NEXO, 27: NEXO, 28: NEXO, 29: NEXO, 30: BIO, 31: BIO,
     32: NEXO, 33: BIO, 34: OCUP, 35: OCUP, 36: OCUP, 37: OCUP, 38: BIO, 39: BIO, 40: NEXO}
d = M["UFG/CS"] = {12: APS, 13: GEST, 14: GEST, 15: IND, 16: IND, 17: GEST, 18: APS, 19: GEST, 20: INF, 21: CV, 22: DD,
     23: DD, 24: DD, 25: CV, 26: CV, 27: EXC, 28: DD, 29: DD, 30: EXC, 43: NEXO, 44: OCUP, 45: OCUP, 46: DERM, 47: OCUP,
     48: OCUP, 49: OCUP, 50: PREV}
faixa(d, 31, 42, OCUP)
M["UPENET/IAUPE"] = {21: CF196, 22: L8142, 23: APS, 24: APS, 25: GEST, 26: GEST, 27: CS, 28: APS, 29: L8080, 30: GEST,
     31: L8080, 32: APS, 33: L8080, 34: GEST, 35: L8080, 36: OCUP, 37: CAP, 38: OCUP, 39: EPI, 40: OCUP, 41: OCUP,
     42: OCUP, 43: CAP, 44: OCUP, 45: OCUP, 46: OCUP, 47: OCUP, 48: BIO, 49: BIO, 50: BIO, 51: BIO, 52: CAP, 53: BIO,
     55: NEXO, 57: BIO, 58: EXAME, 60: OCUP}
d = M["Cebraspe"] = {18: RED, 19: RED, 20: RED, 51: BIO, 52: CAP, 53: CAP, 54: PREV, 55: TEMP, 56: INV, 57: CAP, 58: PREV,
     59: PREV, 60: OCUP, 61: PSI, 62: CV, 63: PSI, 64: NEXO, 65: PSI, 71: BIO, 72: OCUP, 73: EXAME, 78: PREV, 79: CAP,
     80: CAP, 101: APS, 102: APS, 108: BIO, 109: LGPD, 110: LGPD}
faixa(d, 26, 30, DGF); faixa(d, 31, 35, ADM); faixa(d, 41, 42, RESPE); faixa(d, 66, 70, OCUP); faixa(d, 74, 77, OCUP)
faixa(d, 81, 83, PREV); faixa(d, 84, 90, OCUP); faixa(d, 91, 100, PREV); faixa(d, 103, 107, GEST); faixa(d, 111, 118, PREV)

def comando(e):
    if re.search(r"\(\s*\)|\bV\b.*\bF\b|sequ[êe]ncia correta", e): return "V/F ou sequência"
    if re.search(r"afirmativas?|assertivas?|\bI\.\s.*\bII\.", e): return "afirmativas I-II-III"
    if re.search(r"INCORRET|incorreta|\bNÃO\b|EXCETO|exceto", e): return "INCORRETA"
    return "CORRETA"

def main():
    bruto = [json.loads(l) for l in open(os.path.join(BASE, "data", "outras_bruto.jsonl"), encoding="utf-8")]
    out, fora = [], 0
    for q in bruto:
        r = M.get(q["banca"], {}).get(q["numero"])
        if not r: fora += 1; continue
        e = q["enunciado"]
        out.append({**q, "disciplina": r[0], "tema": r[1], "comando": "C/E" if q["formato"] == "C/E" else comando(e),
                    "tipo_enunciado": "situacional" if re.search(r"\d+ anos|paciente|trabalhador|servidor|empregad|segurad", (q.get("contexto", "") + " " + e), re.I) else "direto"})
    with open(os.path.join(BASE, "data", "outras.jsonl"), "w", encoding="utf-8") as f:
        for q in out: f.write(json.dumps(q, ensure_ascii=False) + "\n")
    from collections import Counter
    print(f"outras.jsonl: {len(out)} itens no edital ({fora} fora do edital, de {len(bruto)})")
    print(Counter(q["disciplina"] for q in out)); print(Counter((q["banca"]) for q in out))
    print(Counter(q["tema"] for q in out if q["disciplina"] == "Perícia").most_common())

if __name__ == "__main__":
    main()
