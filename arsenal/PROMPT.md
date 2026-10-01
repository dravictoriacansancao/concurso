# PROMPT — Arsenal de questões IGEDUC · Médico Perito Clínico Geral (Porto Calvo/AL)

> Cole tudo abaixo no Claude Code, dentro de uma pasta vazia (ex.: `~/arsenal-igeduc`). Coloque o PDF do edital nessa pasta antes de rodar.

---

## Missão

Você vai construir, nesta pasta, um **sistema completo de preparação** para a prova objetiva do concurso da Prefeitura de Porto Calvo (AL), Edital 001/2026, banca **Instituto IGEDUC**, cargo **Médico Perito Clínico Geral**.

A prova é no **domingo, 01/11/2026, às 14h**, e dura 4 horas. Hoje é 30/09/2026, então restam cerca de 4 semanas.

O sistema tem cinco partes, nesta ordem:

1. Coletar provas anteriores da banca.
2. Medir estatisticamente o padrão da banca.
3. Estimar a probabilidade de cada tema cair.
4. Gerar um banco grande de questões inéditas no estilo exato da IGEDUC.
5. Entregar um simulador offline que treina onde eu mais perco ponto.

Trabalhe de forma autônoma e em etapas. Ao fim de cada etapa, salve os arquivos, escreva um resumo curto em `LOG.md` e siga para a próxima. Só pare para me perguntar se algo for realmente bloqueante.

---

## Quem vai usar

Sou médica em Alagoas, com pós em Psiquiatria (Einstein). Já atuo como **perita** em avaliações INSS/LOAS/BPC e sou cadastrada como perita judicial na Justiça Federal de Alagoas.

A prática pericial eu domino. Meus pontos fracos prováveis são **legislação do SUS, Direito Constitucional, Informática e as pegadinhas de Português**. Calibre a dificuldade com isso em mente:
- Nas questões de perícia, suba o nível: detalhes normativos e casos-limite, nada de conceito básico.
- Nas demais disciplinas, cubra o edital inteiro e dê atenção extra ao que é decoreba de lei.

---

## Estrutura da prova (fonte: edital, Anexo II e item 3.1.5)

A prova tem 50 questões, com 5 alternativas cada (A–E).

| Grupo | Disciplina | Nº questões | Peso/questão | Total |
|---|---|---|---|---|
| Gerais | Língua Portuguesa | 10 | 1,1 | 11 |
| Gerais | Direito Constitucional | 5 | 1,1 | 5,5 |
| Gerais | Informática | 5 | 1,1 | 5,5 |
| Específicos | Conhecimentos Profissionais (Perícia) | 15 | 2,6 | 39 |
| Específicos | Legislação, Políticas e Gestão do SUS | 15 | 2,6 | 39 |
| | **Total** | **50** | | **100** |

Regras que o simulador precisa aplicar:
- **Eliminação:** total abaixo de 70 pontos, OU nota zero em qualquer disciplina.
- **Desempate 3º critério:** nota em Conhecimentos Profissionais. Os critérios anteriores são idade ≥ 60 anos e títulos.
- Existe **1 vaga**, sem cota. Não basta passar dos 70: o objetivo é ficar em 1º lugar.

### Conteúdo programático exato do edital

Leia também o PDF do edital nesta pasta, para confirmar.

**Português:** fonologia (encontros vocálicos, dígrafos, ortoépia, divisão silábica, prosódia, acentuação, ortografia); interpretação (ideias principais e secundárias, inferência, coesão, coerência, gêneros, variedades linguísticas); morfologia (estrutura e formação de palavras, classes e flexões); redação oficial (ofício, circular, protocolo); semântica (figuras de linguagem, sinonímia, antonímia, homonímia, paronímia, denotação e conotação); sintaxe (termos da oração, período composto, classificação de orações, concordância, regência, crase, pontuação).

**Direito Constitucional:** Administração Pública na CF; aplicabilidade das normas; controle de constitucionalidade; direitos e garantias fundamentais; direitos políticos; federalismo; organização dos Poderes; poder constituinte; princípios fundamentais; processo legislativo; remédios constitucionais; responsabilidade do Estado; segurança pública; sistema tributário nacional; supremacia da Constituição.

**Informática:** editores de texto, planilhas e apresentações; hardware e software; internet, intranet e redes; segurança da informação e proteção de dados; sistemas operacionais (Windows, Linux, macOS); arquivos e pastas; navegadores e buscadores; protocolos; redes sociais e ferramentas colaborativas; vírus e malware; e-mail corporativo; backup; formatação; nuvem; planilhas para cálculo.

**Conhecimentos Profissionais (Perícia):** capacidade laborativa; dano corporal e nexo causal; invalidez e incapacidade permanente; avaliação pericial em doenças cardiovasculares, dermatológicas, endócrinas e metabólicas, infecciosas, neurológicas, osteomusculares, psiquiátricas e respiratórias; bioética aplicada à perícia; CID-10 e CID-11; diagnóstico diferencial; doenças crônicas incapacitantes; doenças ocupacionais; epidemiologia clínica aplicada; exame clínico pericial; incapacidade temporária e permanente; interpretação de exames complementares; medicina baseada em evidências; nexo técnico epidemiológico (NTEP); perícia previdenciária; prognóstico funcional; semiologia pericial.

**SUS:** APS e ESF; CF/88 arts. 196–200; controle social (Conselhos e Conferências); financiamento e aplicação mínima de recursos; gestão municipal do SUS; indicadores e monitoramento; Lei 8.080/1990; Lei 8.142/1990.

### Base normativa a usar

Baixe sempre o **texto vigente** em planalto.gov.br ou no site do órgão oficial:
- CF/88, com atenção aos arts. 1º–17, 18–43, 37–41, 59–69, 102–103, 144, 145–162 e 196–200
- Lei 8.080/1990; Lei 8.142/1990; LC 141/2012 (mínimos em saúde); Decreto 7.508/2011 (regiões de saúde, RENASES, COAP)
- PNAB (Portaria de Consolidação nº 2/2017, Anexo XXII, que incorpora a Portaria 2.436/2017)
- Perícia: Lei 8.213/1991 (incluindo art. 21-A, NTEP); Decreto 3.048/1999; LOAS (Lei 8.742/1993, art. 20, BPC); Código de Ética Médica (Res. CFM 2.217/2018, cap. XI, "Auditoria e Perícia Médica", e demais capítulos aplicáveis); CPC arts. 156–158 e 464–480 (prova pericial)
- Se houver norma posterior relevante até outubro/2026, inclua e registre no LOG

---

## O que já sei sobre o estilo da banca

Isto veio da análise de cerca de 40 questões reais da IGEDUC de 2026 (Prefeituras de Salgueiro/PE e Paulo Afonso/BA). Use como hipótese inicial e **confirme ou corrija com os dados que você coletar**.

1. **Nível superior = questão situacional longa.** O enunciado descreve um cenário ("Durante…", "Em determinado município…"), depois diz "Considerando [tema]" e termina com "**assinale a afirmativa CORRETA**".
2. **As 5 alternativas têm tamanho e estrutura parecidos.** Todas começam com o mesmo sujeito ("A avaliação deve…", "O diagnóstico institucional pode…"), para que não dê para acertar pela forma.
3. **Os distratores são meias-verdades com uma palavra que restringe ou absolutiza:** *exclusivamente, principalmente, por si só, suficiente, independentemente, desde que, dispensa, prioritariamente, restringe, apenas, sendo desnecessário*.
4. **A correta costuma ser a mais integradora e equilibrada:** "considerar conjuntamente…", "articulando X, Y e Z…", "envolve A e B…", "deve ser avaliada quanto aos riscos… antes de…".
5. **Nível médio e técnico é mais direto:** "Qual…?" com uma resposta objetiva e distratores absurdos. Isso não se aplica ao meu cargo, mas serve de contraste.
6. **A letra correta é equilibrada.** Na amostra de 40 questões: A=8, B=7, C=8, D=8, E=9. Não há vício de letra, então chutar sempre a mesma letra não ajuda.
7. **Poucas questões pedem número de artigo.** A banca cobra o conceito aplicado a uma situação.

---

## ETAPA 1 — Coleta de provas anteriores

**Fonte primária: site oficial da banca.** Cada concurso fica em `https://igeduc.org.br/informacoes/<ID>/`. Os IDs vão aproximadamente de 1 a 150; o meu concurso é o 105. Cada página lista:
- "Cadernos de Questões" (um PDF por cargo)
- "Gabaritos" (o gabarito definitivo em PDF, além das respostas a recursos com questões anuladas ou alteradas)

Os PDFs ficam em `anexos.cdn.selecao.net.br` ou `anexos-r2.selecao.net.br`.

Um exemplo confirmado: Japaratinga/AL 2025 (ID 95), que tem caderno de **MEDICO CLINICO GERAL** e gabarito definitivo.

**Procedimento:**
1. Varra `igeduc.org.br/informacoes/1..160/` com um delay educado (1 a 2 s entre requisições) e um User-Agent de navegador comum. Monte `data/concursos.csv` com id, município/UF, ano e a lista de cadernos e gabaritos com URL.
2. Baixe, nesta ordem de prioridade:
   - Cadernos de **Médico** (qualquer especialidade), **Médico Perito** (se existir), **Enfermeiro**, **Fisioterapeuta**, **Psicólogo**, **Farmacêutico**, **Nutricionista** e outros de saúde de nível superior, porque trazem o bloco de SUS.
   - Cadernos de qualquer cargo de **nível superior**, para Português, Constitucional e Informática.
   - Todos os **gabaritos definitivos** e as respostas a recursos (questões anuladas ou alteradas).
3. Salve em `data/raw/<id>_<municipio>_<cargo>.pdf`.
4. Se o site bloquear o download automatizado, **use o navegador** (Claude in Chrome, se estiver disponível) para abrir e baixar. Se nada funcionar, me dê uma lista curta de URLs para eu baixar à mão e continue com o que tiver.

**Fonte secundária, só para metadados e contagem de assuntos:** as páginas públicas de prova do QConcursos (`qconcursos.com/questoes-de-concursos/provas/igeduc-...`) mostram "o que mais caiu" por prova. Use apenas a contagem de assuntos, sem copiar o conteúdo protegido do site.

**Meta mínima:** 8 cadernos de nível superior da área da saúde, com gabarito, de 2024 a 2026. O ideal são 15 ou mais.

## ETAPA 2 — Extração e estruturação

1. Extraia o texto com `pdftotext -layout`. Se o PDF for escaneado, use OCR (`ocrmypdf` ou `tesseract` com `-l por`).
2. Faça o parse em questões: número, disciplina (pelo cabeçalho do caderno), enunciado e alternativas A a E.
3. Cruze cada questão com o gabarito do mesmo cargo e da mesma data de aplicação. Atenção: um gabarito pode cobrir vários cargos e turnos, e questões anuladas devem ser marcadas.
4. Classifique cada questão em **disciplina → tema → subtema**, usando exatamente a taxonomia do meu edital (as listas acima). Quando não encaixar, use "fora do edital".
5. Salve em `data/historico.jsonl`, um objeto por questão, com os campos: `fonte`, `ano`, `cargo`, `disciplina`, `tema`, `subtema`, `enunciado`, `alternativas`, `gabarito`, `anulada`, `tipo_enunciado` ("situacional" ou "direto"), `comando` ("CORRETA", "INCORRETA" ou "EXCETO") e `norma_citada`.
6. Crie `scripts/validar_parse.py`, que confere se toda questão tem 5 alternativas e um gabarito. Rode o script e corrija o que falhar.

## ETAPA 3 — Raio-X estatístico da banca

Gere `relatorio/raio-x.md`, com os gráficos em `relatorio/img/`, contendo:

1. **Frequência por tema**, com o percentual das questões de cada disciplina, separado em SUS e em Constitucional, Informática e Português.
2. **Distribuição da letra correta**, geral e por prova, com teste qui-quadrado contra a distribuição uniforme. Diga claramente se existe vício de letra ou não.
3. **Estatística dos distratores:**
   - frequência de palavras restritivas nas alternativas erradas comparada às certas (tabela de palavras com razão de chance);
   - posição da alternativa mais longa, e com que frequência ela é a correta;
   - com que frequência a correta é a mais "integradora" (mais conectivos aditivos, sem absolutos).
4. **Comando da questão:** proporção de "CORRETA" contra "INCORRETA/EXCETO".
5. **Situacional contra direto** por disciplina.
6. **Artigos e leis mais cobrados** no bloco de SUS (por exemplo, Lei 8.080 arts. 7º e 17–19, Lei 8.142 art. 1º).
7. **Repetição:** temas ou alternativas que reaparecem quase idênticos entre provas diferentes (similaridade de texto acima de 0,8).
8. **Heurísticas de chute validadas:** para cada heurística (eliminar absolutos, escolher a mais integradora, e outras), calcule a taxa de acerto real no histórico. Liste só as que batem acima de 20%, que é o acaso, e diga quanto acima.

## ETAPA 4 — Matriz de probabilidade

Crie `data/matriz.csv`, uma linha por subtema do meu edital, com:

- `p_historico`: frequência do subtema nas provas IGEDUC, com suavização bayesiana (prior uniforme dentro da disciplina, para temas que nunca apareceram não ficarem com zero).
- `peso_edital`: 2,6 para específicas e 1,1 para gerais.
- `pontos_esperados` = p × nº de questões da disciplina × peso.
- `dificuldade_para_mim`: comece com uma estimativa (perícia baixa; SUS, Constitucional e Informática médias ou altas) e **atualize com meu desempenho no simulador**.
- `prioridade` = pontos_esperados × (1 − taxa de acerto atual).

Com isso, gere `relatorio/plano-estudo.md`: um cronograma dia a dia de 01/10 a 31/10/2026, ordenado por prioridade, com meta de questões por dia, revisão espaçada (1, 3, 7 e 14 dias) e 3 simulados completos cronometrados (≈ 17/10, 24/10 e 29/10). Considere de 1h30 a 2h por dia útil e de 4 a 5h no fim de semana.

## ETAPA 5 — Geração do banco de questões inéditas

**Meta: pelo menos 600 questões**, distribuídas proporcionalmente à `prioridade`, com estes mínimos:
- SUS: 180
- Perícia: 180
- Constitucional: 80
- Português: 100
- Informática: 60

**Regras de redação, com a IGEDUC como molde:**
1. 5 alternativas, uma única correta, todas com tamanho parecido (diferença de no máximo 25% em número de caracteres) e começando com a mesma estrutura sintática.
2. Pelo menos 70% situacionais nas específicas, terminando em "assinale a afirmativa CORRETA". Entre 10 e 15% com comando "INCORRETA" ou "EXCETO".
3. Distratores construídos pelo padrão medido na Etapa 3: meia-verdade + palavra restritiva, inversão de competência (União, Estado, Município), troca de prazo ou número, troca de conceito vizinho (incapacidade × deficiência, nexo causal × concausa, eficácia × efetividade).
4. **Letra da correta sorteada uniformemente.** Confira no final se a distribuição ficou entre 18 e 22% por letra.
5. Português: textos-base originais de 150 a 300 palavras, com 3 a 4 questões por texto, no mesmo formato do caderno.
6. Informática: foco em Windows, Word, Excel e navegadores, com fórmulas e atalhos de verdade (PT-BR).
7. Perícia: casos clínicos periciais realistas (INSS, BPC, servidor municipal, judicial) com dados de exame, CID e atividade laboral. Cobre DII/DID, nexo, NTEP, incapacidade parcial/total e temporária/permanente, reabilitação, simulação e dissimulação, e ética pericial (impedimentos e suspeição, perito × assistente técnico).
8. **Não copie** questões do histórico. Use o histórico só como molde de estilo e de tema.

**Cada questão**, em `data/banco.jsonl`, deve ter: `id`, `disciplina`, `tema`, `subtema`, `dificuldade` (1–3), `enunciado`, `alternativas{A..E}`, `gabarito`, `comentario_correta`, `por_que_cada_errada{A..E}`, `fundamento` (lei, artigo e inciso, ou referência técnica), `pegadinha` (qual armadilha da banca a questão treina) e `prob_tema` (da matriz).

**Controle de qualidade, obrigatório:**
1. `scripts/qa_banco.py` checa: formato, 5 alternativas, tamanho parecido, distribuição de letras, duplicatas por similaridade acima de 0,85, e presença do fundamento.
2. **Revisão cega:** para cada lote de 50 questões, resolva as questões **sem ver o gabarito**, conferindo contra o texto da lei baixado. Toda questão em que sua resposta divergir do gabarito, ou em que mais de uma alternativa seja defensável, deve ser **corrigida ou descartada**. Registre a taxa de descarte no LOG.
3. Nas questões de lei, o comentário deve **citar o dispositivo e conferir o texto vigente**. Na dúvida sobre redação atual, marque `verificar: true` em vez de inventar.

## ETAPA 6 — Simulador

Crie `simulador/index.html`, um **arquivo único e offline**, com o banco embutido em JSON. Precisa funcionar no navegador do celular e do computador, e ter:

- **Modo Treino:** filtros por disciplina, tema e dificuldade; opção "só as que errei"; correção imediata com comentário, o porquê de cada errada e a pegadinha.
- **Modo Simulado:** 50 questões na proporção exata da prova (10/5/5/15/15), cronômetro de 4h, gabarito só no final, pontuação com os pesos 1,1 e 2,6, e indicação de **aprovada ou eliminada** (abaixo de 70, ou zero em alguma disciplina).
- **Modo Revisão Espaçada:** as questões erradas voltam em 1, 3, 7 e 14 dias.
- **Painel:** acerto por disciplina e por tema, pontos projetados na prova real, tempo médio por questão, e os temas que mais custam pontos (ordenados por `prioridade`).
- **Treino de chute:** mostra só as alternativas, sem o enunciado, e pede para eu apontar a mais provável pelas heurísticas da Etapa 3. Serve para eu calibrar o instinto.
- Salve o progresso em `localStorage` (com try/catch) e ofereça botões para **exportar e importar** o progresso em JSON, para eu passar do celular para o computador.
- Tema claro e escuro, fonte legível, botões grandes para uso no celular.

Também gere:
- `simulador/banco.pdf`, com todas as questões e o gabarito comentado no final, para estudar impresso;
- `simulador/flashcards.csv` (frente;verso), com os pontos de lei mais cobrados, para importar no Anki.

## ETAPA 7 — Entrega

Ao final, crie `README.md` explicando:
1. Como abrir o simulador (basta dar dois cliques no `index.html`).
2. Como gerar mais questões de um tema específico, com o comando `python scripts/gerar.py --tema "<tema>" --n 30`. Deixe esse script pronto para chamar você (Claude) de novo com as mesmas regras de estilo e de controle de qualidade.
3. Como atualizar a matriz de prioridade com meu progresso exportado, com `python scripts/atualizar_matriz.py progresso.json`.

Depois me mostre um resumo final com:
- quantas provas e questões históricas foram coletadas;
- os 5 achados mais úteis do raio-X;
- quantas questões inéditas foram geradas, por disciplina, e quantas foram descartadas no controle de qualidade;
- os 10 temas de maior prioridade para as próximas 4 semanas.

---

## Restrições gerais

- Idioma: português do Brasil em tudo.
- Não invente dados estatísticos. Se a amostra for pequena, diga o N e o intervalo de confiança.
- Não invente lei. Todo fundamento legal precisa vir do texto oficial baixado.
- Se alguma fonte estiver indisponível, registre no LOG e continue com o restante.
- Faça commits (git) ao fim de cada etapa, para eu poder voltar atrás.
