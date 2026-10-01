# Provas de MÉDICO PERITO de outras bancas

A IGEDUC nunca aplicou prova de perito, então fui buscar **o que outras bancas cobram de perito médico** e
transformei isso em treino. Estas questões **não entram no Treino de chute**, que continua só com questões
originais da IGEDUC.

Scripts: `gabaritos_outras.py` → `coletar_outras.py` → `classificar_outras.py` · Dados: `data/outras.jsonl`

## Amostra: 7 provas, 435 questões, 279 no seu edital

| Banca | Concurso | Formato | Questões | No seu edital |
|---|---|---|---|---|
| **Cebraspe** | Perito Médico Federal (MPS) 2025 | Certo/Errado | 120 | 83 |
| **FGV** | Macaé/RJ 2024 | A–E | 70 | 40 |
| **UFG/CS** | Goiânia/GO 2022 | A–D | 50 | 39 |
| **UPENET/IAUPE** | Olinda/PE 2024 | A–E | 60 | 37 |
| **CEV-URCA** | Várzea Alegre/CE 2024 | A–E | 55 | 30 |
| **Instituto UniFil** | Paranaguá/PR 2022 | A–D | 40 | 30 |
| **FUNDATEC** | Nova Santa Rita/RS 2023 (perito psiquiatra) | A–E | 40 | 20 |

- Gabaritos oficiais definitivos, exceto FUNDATEC (só existe o preliminar; marcado no simulador).
- Todas as 435 questões foram extraídas e conferidas contra o gabarito.
- **Ficaram de fora 156 questões** que não estão no seu edital: Português com texto-base (o texto não vem junto),
  conhecimentos locais e atualidades, matemática, legislação municipal e de servidor, ética do servidor.
- No simulador entram **272** (as 7 anuladas saem): Treino → origem "Provas de perito (outras bancas)".

## O que as outras bancas cobram de perito

| Bloco | Questões |
|---|---|
| **Perícia / saúde do trabalhador / clínica** | **196** |
| SUS | 58 (gestão e políticas 22, Lei 8.080 15, APS 9) |
| Constitucional | 20 |
| Português (Redação Oficial) e Informática (LGPD) | 5 |

### Dentro de perícia (menções; uma questão pode tocar 2 assuntos)
| Assunto | Menções |
|---|---|
| Clínica aplicada (cardio, psiquiatria, endócrino, infecto) | 50 |
| **NR 7 / PCMSO / exames ocupacionais (admissional, retorno, demissional, ASO)** | **34** |
| BPC/LOAS, avaliação biopsicossocial, pessoa com deficiência | 24 |
| Código de Ética Médica, documentos, sigilo, telemedicina | 23 |
| Insalubridade (NR 15), agentes físicos/químicos/biológicos, NR 31/32 | 21 |
| Benefícios por incapacidade, carência, qualidade de segurado | 19 |
| DII/DID, capacidade laborativa, retorno ao trabalho | 19 |
| Ruído, PAIR, audiometria | 15 |
| LER/DORT, ergonomia, telemarketing | 12 |
| Saúde mental e trabalho (burnout, assédio, TEPT) | 9 |
| Laudo pericial, CPC, deveres do perito | 9 |
| Pneumoconioses, asma ocupacional | 8 |
| Acidente de trabalho, CAT, trajeto | 8 |
| PGR / NR 1 / riscos | 7 |
| Nexo causal, concausa, NTEP, Schilling | 6 |
| Medicina legal / traumatologia forense | 6 |
| Doença grave, isenção de IR, cardiopatia grave | 3 |

**Recado:** perícia de prefeitura = **medicina do trabalho + previdenciária + ética**. NR 7 é o tema mais
repetido entre bancas diferentes.

## 25 inéditas novas no estilo IGEDUC (A–E)
Escritas a partir dos buracos que esse raio-X mostrou no banco (`fonte/pericia_outras.py`, PER-042 a PER-066).
Sempre que o tema caiu numa dessas provas, o fato foi ancorado no gabarito oficial:

- NR 7: demissional (dispensa em 135/90 dias), retorno (30 dias, antes de reassumir), audiometria, ASO × sigilo
- NR 15: graus (radiação ionizante máximo, calor médio), quantitativo × qualitativo, 85 dB = 8 h, não cumula adicionais
- NR 1 (PGR), NR 32 (reencape vedado), NR 17 telemarketing (6 h)
- Schilling, pneumoconioses (OIT), TEPT (latência)
- Período de graça, BPC não mantém qualidade de segurado, reaquisição de carência (metade), estabilidade
  acidentária (mínimo 12 meses), auxílio-acidente por PAIR, BPC (revisão a cada 2 anos), isenção de IR
- CEM: sigilo em exame ocupacional (art. 76), honorário de êxito (art. 96), CPC art. 473, capacidade × diagnóstico
- 6 delas são de comando INCORRETA/EXCETO, que estava quase ausente do banco.

## Padrões de banca (só como curiosidade; NÃO valem para a IGEDUC)
- Letra da correta equilibrada também aqui (A–E: A 47, B 44, C 42, D 50, E 38).
- Cebraspe: 63 Errado × 49 Certo. Os "errados" típicos trocam mínimo/máximo, "sempre", "independentemente".
- Comando: as outras bancas usam muito mais "afirmativas I-II-III" (41) e INCORRETA/EXCETO (24) que a IGEDUC.

## Limitações
- Classificação de tema feita item a item, à mão; "menções" acima usam palavras-chave, são aproximadas.
- O gabarito da FUNDATEC é preliminar.
- Estilo, tamanho de alternativas e pegadinhas variam por banca. Para o "jeito IGEDUC", use as questões reais
  da IGEDUC e o Treino de chute.
