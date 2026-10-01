"""Etapa 2b: deduplica cadernos idênticos e classifica cada questão real na taxonomia do edital.
Entrada: data/historico_bruto.jsonl · Saída: data/historico.jsonl"""
import json, os, re
BASE = os.path.join(os.path.dirname(__file__), "..")
FORA = "fora do edital"

POR = "Português"; CON = "Constitucional"; INF = "Informática"; SUS = "SUS"; CLI = "Clínica (outro cargo)"
MAPA = {
 114: {**{n: (POR, "Interpretação e Análise Textual") for n in (2, 5, 8, 10)},
       **{n: (POR, "Sintaxe") for n in (1, 3, 4, 7)}, **{n: (POR, "Fonologia") for n in (6, 9)},
       11: (INF, "Utilização de planilhas eletrônicas"), 12: (INF, "Aplicativos de escritório"),
       13: (INF, "Conceitos de segurança da informação e proteção de dados"), 14: (INF, "Conceitos de sistemas operacionais"),
       15: (INF, "Aplicativos de escritório"), 16: (INF, "Conceitos de segurança da informação e proteção de dados"),
       17: (INF, "Utilização de planilhas eletrônicas"), 18: (INF, "Conceitos sobre redes sociais e ferramentas colaborativas"),
       19: (INF, "Ferramentas de backup e recuperação de dados"), 20: (INF, "Utilização de planilhas eletrônicas"),
       **{n: (CLI, FORA) for n in range(21, 36)},
       36: (SUS, "APS e ESF"), 37: (SUS, "Gestão municipal do SUS"), 38: (SUS, "Lei nº 8.080/1990"),
       39: (SUS, "Gestão municipal do SUS"), 40: (SUS, "Lei nº 8.080/1990")},
 142: {1: (POR, "Sintaxe"), 2: (POR, "Interpretação e Análise Textual"), 3: (POR, "Interpretação e Análise Textual"),
       4: (POR, "Sintaxe"), 5: (POR, "Sintaxe"), 6: (POR, "Morfologia"), 7: (POR, "Interpretação e Análise Textual"),
       8: (POR, "Sintaxe"), 9: (CON, "Organização dos Poderes"), 10: (CON, "Administração Pública na CF"),
       11: (CON, "Direitos e garantias fundamentais"), 12: (CON, "Direitos e garantias fundamentais"),
       13: (CON, "Aplicabilidade e interpretação das normas"), 14: (CON, "Organização dos Poderes"),
       15: (CON, "Princípios fundamentais"), 16: (CON, "Federalismo e organização do Estado"),
       17: (CON, "Administração Pública na CF"), 18: ("Ética e serviço público", FORA), 19: ("Ética e serviço público", FORA),
       20: ("Ética e serviço público", FORA), 21: (CON, "Administração Pública na CF"), 22: ("Ética e serviço público", FORA),
       23: ("Ética e serviço público", FORA), 24: (INF, "Conceitos de segurança da informação e proteção de dados"),
       25: (INF, "Conceitos de segurança da informação e proteção de dados"), 26: (INF, "E-mail e comunicação eletrônica no ambiente corporativo"),
       27: (INF, "Conceitos de segurança da informação e proteção de dados"), 28: (INF, "Conceitos básicos de hardware e software"),
       29: (INF, FORA), 30: (INF, "Conceitos sobre redes sociais e ferramentas colaborativas")},
 95: {**{n: (POR, "Interpretação e Análise Textual") for n in (1, 2, 3, 5, 6, 9, 10)},
      4: (POR, "Sintaxe"), 7: (POR, "Sintaxe"), 8: (POR, "Fonologia"),
      11: (INF, "Conceitos sobre protocolos de comunicação na internet"),
      **{n: (INF, "Conceitos de segurança da informação e proteção de dados") for n in (12, 13, 14, 18)},
      **{n: (INF, "Utilização de planilhas eletrônicas") for n in (15, 16, 17)},
      19: (INF, "Aplicativos de escritório"), 20: (INF, "Aplicativos de escritório"),
      **{n: (CLI, FORA) for n in range(21, 36)},
      36: (SUS, FORA), 37: (SUS, "Lei nº 8.080/1990"), 38: ("Ética e serviço público", FORA),
      39: (SUS, "Gestão municipal do SUS"), 40: (SUS, FORA)},
}

def comando(e):
    if re.search(r"\bV\b.*\bF\b|sequ[êe]ncia correta", e): return "V/F ou sequência"
    if re.search(r"proposi[çc][õo]es|afirmativas? (I|II)|\bI, II\b", e): return "afirmativas I-II-III"
    if re.search(r"INCORRET|\bNÃO\b|EXCETO", e): return "INCORRETA"
    return "CORRETA"

def tipo(e):
    return "situacional" if re.search(r"^(Um|Uma|Em um|Em uma|Durante|Ao |Matheus|[A-Z][a-z]+ é )|paciente de \d+|trabalhador", e) else "direto"

def main():
    bruto = [json.loads(l) for l in open(os.path.join(BASE, "data", "historico_bruto.jsonl"), encoding="utf-8")]
    vistos, out = set(), []
    for q in bruto:
        chave = (q["concurso"], q["numero"])
        if chave in vistos:   # Cabo/PE: o mesmo caderno foi aplicado a PSF, Trabalho e Psiquiatra
            continue
        vistos.add(chave)
        d, t = MAPA[q["concurso"]][q["numero"]]
        normas = sorted(set(re.findall(r"Lei n?º? ?[\d.]+/\d{4}|art\. ?\d+", q["enunciado"])))
        q.update(disciplina=d, tema=t, tipo_enunciado=tipo(q["enunciado"]), comando=comando(q["enunciado"]),
                 norma_citada=normas, cargos_mesmo_caderno=None)
        if q["concurso"] == 142:
            q["cargo"] = "MEDICO (PSF / TRABALHO / PSIQUIATRA – caderno único)"
        out.append(q)
    with open(os.path.join(BASE, "data", "historico.jsonl"), "w", encoding="utf-8") as f:
        for q in out: f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(f"historico.jsonl: {len(out)} questões únicas (de {len(bruto)} extraídas)")

if __name__ == "__main__":
    main()
