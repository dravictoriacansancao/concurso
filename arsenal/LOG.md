# LOG do arsenal

## 2026-10-01 · Execução inicial

**Etapa 0 – teste de acesso.** Bloqueados no ambiente: igeduc.org.br, *.selecao.net.br, qconcursos.com,
planalto.gov.br, in.gov.br, portal.cfm.org.br, gov.br, normas.leg.br, camara/senado. Liberados: pypi.org.

**Etapas 1–3 (coleta, parse, raio-X): NÃO EXECUTADAS.** Sem acesso às provas. `data/historico.jsonl` não existe.
Registrado em `relatorio/raio-x.md` com o caminho para destravar. Nenhuma estatística foi inventada.

**Etapa 4 – matriz.** `data/matriz.csv` com 67 temas do edital. Sem histórico (N = 0), `p_historico` usa prior
uniforme dentro da disciplina (Laplace). Taxa de acerto inicial estimada: Perícia 80%, Português 60%,
SUS 55%, Informática 50%, Constitucional 45%. A prioridade passa a usar o acerto real com ≥ 5 respostas.
`relatorio/plano-estudo.md`: cronograma 01/10–31/10 com simulados em 17/10, 24/10 e 29/10.

**Etapa 5 – banco (lote 1).** 123 questões inéditas: SUS 39, Perícia 41, Constitucional 17, Português 13
(2 textos originais), Informática 13. Meta do prompt: 600 → faltam ~477 (próximos lotes).
- Letras: sorteio balanceado por disciplina (A–E entre 18% e 22%).
- **Vício encontrado e corrigido:** a correta era a alternativa mais longa em 67% das questões. Reescritas
  79 corretas e 15 distratores → agora 16% (acaso = 20%).
- Avisos de tamanho (diferença > 25% entre alternativas) restam em parte das questões; a correta não é
  mais identificável pelo tamanho.
- Descarte no controle de qualidade: 1 distrator reescrito (MP sobre direito penal "para beneficiar o réu",
  defensável pela jurisprudência do STF) → trocado. Taxa de descarte de questões: 0/123.
- **Revisão cega:** feita pelo próprio autor (resolução sem olhar o gabarito, conferindo a lei de memória).
  Não é independente e o texto oficial das leis não pôde ser baixado. 9 questões ficaram `verificar: true`
  (redação a conferir no Planalto). Todas as questões geradas por `scripts/gerar.py` entram como verificar.
- Pendências para os próximos lotes: INCORRETA/EXCETO só 2% (meta 10–15%); SUS situacional 59% (meta 70%).

**Etapa 6 – simulador.** `simulador/index.html` (offline, arquivo único, 257 KB) com Treino, Simulado
(10/5/5/15/15, 4 h, pesos 1,1/2,6, regra de eliminação), Revisão espaçada (1/3/7/14 dias), Painel,
Treino de chute (destaca palavras absolutas) e exportar/importar progresso. Teste automatizado no
Chromium a 400 px: sem erros de script, sem rolagem horizontal; simulado com todas as respostas "C"
→ 21,5 pontos e "Eliminada · zerou disciplina", como esperado. `banco.pdf` e `flashcards.csv` (110 cartões).

**Etapa 7 – entrega.** README, `scripts/gerar.py` (Claude Opus 5.5 via API, JSON estruturado, fallback de
recusa), `scripts/atualizar_matriz.py` (testado com progresso de exemplo).

## 2026-10-01 · Provas reais (etapas 1–3)

**Coleta:** 5 PDFs enviados pela Victoria (caderno + gabarito), salvos em `data/raw/`.
**Extração:** texto por coluna (`pdftotext` com recorte da página); 170 questões, todas com 4 alternativas.
**Gabaritos:** transcrição de cada PDF conferida contra o bloco oficial do mesmo PDF: 5/5 idênticos.
**Duplicatas:** os 3 cadernos de Cabo de Santo Agostinho (PSF, Trabalho, Psiquiatra) têm o mesmo gabarito
letra por letra → caderno único; contado uma vez. Resultado: 110 questões únicas, 4 anuladas, 106 válidas.
**Classificação:** manual por número de questão (`scripts/classificar_historico.py`); 36 fora do edital do perito
(clínica e ética). `scripts/validar_parse.py historico.jsonl` → OK.
**Raio-X:** `relatorio/raio-x.md`. Achados: sem vício de letra (p = 0,78); correta é a mais longa em 43%
(acaso 25%); "menos absolutos" acerta 48% (68% em SUS/clínica); "exclusivamente" e "sempre" nunca na correta;
INCORRETA só 1%; formato de 4 alternativas (Porto Calvo terá 5).
**Matriz:** `data/matriz.csv` agora usa a frequência real de temas (suavização de Laplace).
**Simulador:** 106 questões reais adicionadas (Treino com filtro de origem; Treino de chute usa as reais;
Simulado continua só com inéditas, no formato de 5 alternativas). Teste no Chromium: sem erros.

**Observação para os próximos lotes de inéditas:** a banca real TEM o padrão "correta mais longa/completa".
O lote 1 foi neutralizado de propósito (16%). Decidir se os próximos lotes devem reproduzir o padrão real.

## 2026-10-01 · Lote 2 de provas reais (zip "Arquivo 2")

**Coleta:** 13 cadernos separados + 3 gabaritos definitivos oficiais (concursos 95, 114, 142). Os PDFs
"caderno+gabarito" antigos foram substituídos pelos cadernos limpos; o gabarito agora vem sempre do PDF oficial.
**Extração:** 460 questões; limpeza de rodapé ("CARGO - 1") e da marca d'água de Cabo ("RASCUNHO / PREFEITURA…").
**Deduplicação:** mesma questão aparece em vários cargos com alternativas embaralhadas → comparação por enunciado +
conjunto de alternativas (≥ 85% de similaridade) e conferência do texto da correta: 0 conflitos. 192 únicas, 4 anuladas.
**Classificação:** por estrutura da prova (95/114: 1–10 Port, 11–20 Inf, 21–35 específicas, 36–40 legislação;
142: só gerais) + regras de conteúdo + 8 ajustes manuais após revisão.
**Raio-X atualizado (n = 188):** sem vício de letra (p = 0,53); mais integradora 44%, menos absolutos 42%,
mais longa 39% (acaso 25%); "exclusivamente" 0 em 188 corretas × 24 erradas; V/F 18%; INCORRETA 0,5%.
As pistas enfraqueceram em relação ao lote 1 (n maior): o relatório explica.
**Simulador:** 188 reais. Corrigido: simulado podia montar 49 questões (agrupamento de textos de Português).
