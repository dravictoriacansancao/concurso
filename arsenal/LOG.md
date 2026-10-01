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

## 2026-10-01 · Lote 3: todas as provas de médico da IGEDUC (zip "IGEDUC_medicos_NOVOS")

**Mapa:** o Claude in Chrome varreu os concursos 1–191 da banca (`relatorio/mapa-igeduc.md`). Nenhum concurso anterior
teve perito médico; Porto Calvo (nº 105) é o primeiro.
**Coleta:** +43 cadernos de 16 concursos. Total: 21 concursos, 49 cadernos, 2.820 itens, 1.980 únicos.
**Formatos novos:** V/F (2022–2024: Ingá, Triunfo, Surubim, Pombos, Salgueiro 2024, Cupira) e 5 alternativas
(2026: Terezinha, Pão de Açúcar, Paulo Afonso, Altos, Terra Nova, Salgueiro 2026), além de 4 alternativas.
**Correções na extração:** escolha automática entre pdftotext e pdfplumber por coluna (letras espaçadas); itens de
V/F sem zero à esquerda (Cupira); número no fim de linha engolindo item (Ingá); instruções numeradas da capa
confundidas com itens 1–4; "X" = anulada (Paraíso do Norte); títulos "CONHECIMENTOS…" grudados em alternativas.
Descartado: Paraíso do Norte Q44 (alternativas em tabela). Gabaritos divergentes entre cargos: nenhum.
**Classificação:** regras de conteúdo + revisão manual dos 42 itens marcados como Perícia (7 falsos positivos
reclassificados → 35 itens). `relatorio/pericia-igeduc.md` lista os 35.
**Raio-X (n = 886 múltipla escolha + 1.077 V/F):** sem vício de letra (p = 0,71 e 0,83); mais integradora 42%
(39% no formato A–E, acaso 20%); "exclusivamente" 0 × 88; SUS = 344 itens (bloco mais cobrado).
**Matriz:** prioridades agora usam a frequência real (Lei 8.080 e APS/ESF no topo).
**Simulador:** 1.963 itens reais (4, 5 alternativas e V/F); filtro por disciplina inclui Perícia (35 reais).

## 2026-10-01 · Lote 4: provas de perito de outras bancas (zip "PERITO_OUTRAS_BANCAS")

**Coleta:** 7 provas de médico perito (Cebraspe/MPS 2025, FGV/Macaé 2024, UFG/Goiânia 2022, UPENET/Olinda 2024,
CEV-URCA/Várzea Alegre 2024, UniFil/Paranaguá 2022, FUNDATEC/Nova Santa Rita 2023), em `data/raw_outras/`.
**Extração:** um leitor de gabarito e um marcador de questão por banca; 435/435 questões batem com o gabarito.
Cebraspe e UniFil exigiram `pdftotext -layout` por coluna (o modo simples embaralha a ordem). Acentos soltos da URCA
("opc¸a˜o") normalizados; cabeçalhos e marcas d'água removidos. Itens Cebraspe levam o comando/caso do bloco.
FUNDATEC: só há gabarito preliminar.
**Classificação:** manual, item a item, nos temas do edital → 279 no edital (196 de Perícia); 156 fora.
**Simulador:** +272 itens (sem anuladas) com origem "Provas de perito (outras bancas)". Treino de chute continua
só com questões originais da IGEDUC (filtro por `banca === "IGEDUC"`).
**Inéditas:** +25 (PER-042 a PER-066) sobre NR 7, NR 15, NR 1, NR 32, NR 17, Schilling, pneumoconioses, TEPT,
qualidade de segurado, carência, estabilidade, auxílio-acidente, BPC, isenção de IR e CEM. 6 de comando INCORRETA.
Relatório: `relatorio/outras-bancas.md`.
**Privacidade:** os 6 PDFs baixados do PCI Concursos (FUNDATEC, UniFil, UFG) trazem marca d'água com o IP de quem baixou; ficam fora do Git (`.gitignore`). Os dados extraídos estão limpos.

## 2026-10-01 · 3 simulados em PDF

`scripts/simulados_pdf.py` → `simulados/simulado-{1,2,3}.pdf` (+ .html). Cada um: 50 questões A–E na ordem e
distribuição do edital (10 Port · 5 Const · 5 Inf · 15 Perícia · 15 SUS), 4 h, folha de respostas, gabarito,
tabela de nota (pesos 1,1/2,6; corte 70) e gabarito comentado (inéditas com comentário e pegadinha; reais com a
origem). Nenhuma questão se repete entre os três. Mistura ≈ 22 inéditas + 18 reais IGEDUC + 10 de perito de
outras bancas por simulado. Português: só itens reais autocontidos (24 revisados à mão); itens que dependem de
texto não incluído ou com defeito de extração ficaram de fora.
