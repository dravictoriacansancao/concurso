"""Gera mais questões inéditas de um tema, chamando o Claude com as mesmas regras de estilo.

Uso:
    pip install anthropic
    export ANTHROPIC_API_KEY=...        # ou: ant auth login
    python scripts/gerar.py --tema "Lei nº 8.142/1990" --n 30

Grava fonte/gerado_<tema>_<data>.json. Depois rode:
    python scripts/build_banco.py && python scripts/qa_banco.py && python scripts/build_simulador.py
As questões geradas entram marcadas verificar=true até você conferir a lei no Planalto.
"""
import argparse, datetime, json, os, re, sys, unicodedata
import anthropic

BASE = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.dirname(__file__))
from taxonomia import TEMAS

REGRAS = """Você escreve questões inéditas para a prova objetiva do concurso de Porto Calvo (AL), banca IGEDUC,
cargo Médico Perito Clínico Geral. Estilo da banca (nível superior):
1. Enunciado situacional ("Durante…", "Em determinado município…"), depois "Considerando [tema]" e
   termina em "assinale a afirmativa CORRETA". Entre 10% e 15% das questões usam "INCORRETA".
2. Cinco alternativas com tamanho parecido (diferença máxima de 25% em caracteres) e a MESMA estrutura
   inicial. A correta NÃO pode ser sistematicamente a mais longa nem a mais completa.
3. Distratores: meia-verdade + palavra restritiva/absoluta (exclusivamente, apenas, por si só, dispensa,
   independentemente, desde que), inversão de competência (União/Estado/Município), troca de prazo ou
   número, troca de conceito vizinho (incapacidade × deficiência, nexo causal × concausa, eficácia × efetividade).
4. Uma única alternativa defensável. Nada de "todas as anteriores".
5. Fundamento com lei, artigo e inciso (ou referência técnica). Se não tiver certeza da redação vigente,
   marque verificar=true; nunca invente dispositivo.
6. Público: médica que já atua como perita (INSS/BPC/judicial). Nas questões de perícia, cobre detalhe
   normativo e casos-limite, não conceito básico.
Português do Brasil. Não copie questões existentes."""

ESQUEMA = {
    "type": "object", "additionalProperties": False, "required": ["questoes"],
    "properties": {"questoes": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["disciplina", "tema", "subtema", "dificuldade", "tipo_enunciado", "comando", "enunciado",
                     "correta", "erradas", "comentario_correta", "fundamento", "pegadinha", "verificar"],
        "properties": {
            "disciplina": {"type": "string", "enum": list(TEMAS)},
            "tema": {"type": "string"}, "subtema": {"type": "string"},
            "dificuldade": {"type": "integer", "enum": [1, 2, 3]},
            "tipo_enunciado": {"type": "string", "enum": ["situacional", "direto"]},
            "comando": {"type": "string", "enum": ["CORRETA", "INCORRETA"]},
            "enunciado": {"type": "string"}, "correta": {"type": "string"},
            "erradas": {"type": "array", "items": {
                "type": "object", "additionalProperties": False, "required": ["texto", "por_que"],
                "properties": {"texto": {"type": "string"}, "por_que": {"type": "string"}}}},
            "comentario_correta": {"type": "string"}, "fundamento": {"type": "string"},
            "pegadinha": {"type": "string"}, "verificar": {"type": "boolean"}}}}}}

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tema", required=True)
    ap.add_argument("--n", type=int, default=20)
    a = ap.parse_args()
    disc = next((d for d, ts in TEMAS.items() if a.tema in ts), None)
    if not disc:
        raise SystemExit("Tema não está na taxonomia do edital. Opções:\n" + "\n".join(t for ts in TEMAS.values() for t in ts))
    existentes = [json.loads(l)["enunciado"] for l in open(os.path.join(BASE, "data", "banco.jsonl"), encoding="utf-8")
                  if json.loads(l)["tema"] == a.tema]
    pedido = (f"Gere {a.n} questões da disciplina '{disc}', tema '{a.tema}' (use exatamente esses valores nos campos "
              f"disciplina e tema). Cada questão tem exatamente 4 itens em 'erradas'. Varie subtemas e dificuldade.\n\n"
              "Enunciados que JÁ existem neste tema (não repita):\n- " + "\n- ".join(existentes[:60]))
    client = anthropic.Anthropic()
    with client.beta.messages.stream(
        model="claude-opus-5-5",
        max_tokens=64000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        thinking={"type": "adaptive"},
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": ESQUEMA}},
        system=REGRAS,
        messages=[{"role": "user", "content": pedido}],
    ) as stream:
        resp = stream.get_final_message()
    if resp.stop_reason == "refusal":
        raise SystemExit("O modelo recusou o pedido; tente reformular o tema.")
    if resp.stop_reason == "max_tokens":
        raise SystemExit("Resposta cortada; peça menos questões (--n).")
    texto = "".join(b.text for b in resp.content if b.type == "text")
    lote = json.loads(texto)
    lote["questoes"] = [q for q in lote["questoes"] if len(q["erradas"]) == 4 and q["tema"] == a.tema]
    for q in lote["questoes"]:
        q["verificar"] = True  # sempre conferir antes de confiar
    out = os.path.join(BASE, "fonte", f"gerado_{slug(a.tema)}_{datetime.date.today():%Y%m%d}.json")
    json.dump(lote, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(lote['questoes'])} questões em {out}")

if __name__ == "__main__":
    main()
