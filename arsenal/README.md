# Arsenal IGEDUC · Médico Perito Clínico Geral (Porto Calvo/AL)

Prova em **01/11/2026, 14h**. Sistema de preparação: banco de questões inéditas no estilo IGEDUC,
simulador offline, matriz de prioridade e plano de estudo.

## 1. Abrir o simulador
- **Computador:** dois cliques em `simulador/index.html`. Funciona sem internet (a fonte bonita só carrega online).
- **Celular:** use o link da página publicada (enviado na conversa) ou mande o `index.html` para o celular.
- Abas: **Treino** (filtros e correção comentada) · **Simulado** (prova completa de 4 h) · **Revisão** (erradas
  voltam em 1/3/7/14 dias) · **Painel** (pontos projetados e onde você mais perde ponto) · **Treino de chute** ·
  **Progresso** (copiar/colar para passar de um aparelho a outro).
- No Treino, o filtro de origem separa: inéditas · provas reais IGEDUC · **provas de perito (outras bancas)**.
  O Treino de chute usa só questões originais da IGEDUC.
- Para estudar no papel: `simulador/banco.pdf`. Para o Anki: importe `simulador/flashcards.csv` (separador `;`).

## 2. Gerar mais questões de um tema
```bash
pip install anthropic
export ANTHROPIC_API_KEY=...          # ou: ant auth login
python scripts/gerar.py --tema "Lei nº 8.142/1990" --n 30
python scripts/build_banco.py && python scripts/qa_banco.py && python scripts/build_simulador.py
```
Os nomes de tema válidos estão em `scripts/taxonomia.py` (são os do edital). Questões geradas entram
marcadas "conferir lei" até você checar a redação no Planalto.

## 3. Atualizar a prioridade com o seu desempenho
No simulador: **Progresso → Copiar progresso**, cole num arquivo `progresso.json` e rode:
```bash
python scripts/atualizar_matriz.py progresso.json
```
Isso recalcula `data/matriz.csv`, o banco e o simulador.

## Estrutura
| Caminho | Conteúdo |
|---|---|
| `fonte/*.py` | Questões-fonte escritas à mão (correta separada das erradas) |
| `data/banco.jsonl` | Banco final (letras sorteadas, comentários, fundamento, pegadinha) |
| `data/matriz.csv` | Prioridade por tema |
| `relatorio/plano-estudo.md` | Cronograma 01/10–31/10 |
| `relatorio/raio-x.md` | Raio-X da IGEDUC: 21 concursos, 1.980 questões reais |
| `relatorio/pericia-igeduc.md` | Os 35 itens de perícia que a IGEDUC já cobrou |
| `relatorio/outras-bancas.md` | 7 provas de perito de outras bancas: o que cobram (279 questões no edital) |
| `data/historico.jsonl` · `data/outras.jsonl` | Questões reais (IGEDUC / outras bancas) classificadas |
| `LOG.md` | O que foi feito, números e pendências |
| `PROMPT.md` | Prompt original |
