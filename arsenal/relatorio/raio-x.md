# Raio-X da banca IGEDUC (provas reais de médico)

Dados brutos: `relatorio/raio-x-dados.json` · Scripts: `coletar_historico.py` → `classificar_historico.py` → `raio_x.py`
Mapa de todos os concursos da banca: `relatorio/mapa-igeduc.md` · Itens de perícia: `relatorio/pericia-igeduc.md`

## Amostra
- **21 concursos, 49 cadernos (2022–2026), 2.820 itens extraídos → 1.980 únicos** (17 anulados, 1 descartado por
  defeito de extração: Paraíso do Norte Q44, alternativas em tabela).
- Gabaritos sempre do **gabarito definitivo oficial** (Altos/PI 2026: só havia o preliminar).
- Dentro de um concurso, os cargos repetem as mesmas questões com alternativas embaralhadas. Comparei o texto da
  correta em todas as cópias: **nenhuma divergência**. Cada questão foi contada uma vez.

| Formato | Concursos | Itens únicos |
|---|---|---|
| **5 alternativas (A–E)** — 2026, igual à sua prova | Terezinha, Pão de Açúcar, Paulo Afonso, Altos, Terra Nova, Salgueiro 2026 | 322 |
| 4 alternativas (A–D) — 2024–2026 | Japaratinga, S. J. do Seridó, Cabo, Calumbi, Paraíso do Norte, Flores, Craíbas, Serraria, Jati | 580 |
| Verdadeiro/Falso — 2022–2024 | Ingá, Triunfo, Surubim, Pombos, Salgueiro 2024, Cupira | 1.078 |

**A IGEDUC nunca aplicou prova de perito médico.** Porto Calvo é a primeira. Ninguém tem prova anterior de perícia da banca.

## 1. O que cai
| Disciplina | Itens | Detalhe |
|---|---|---|
| **SUS** | **344** | Lei 8.080 (103), APS/ESF (97), indicadores e vigilância (43), gestão municipal (31), controle social (26), financiamento (15) |
| Português | 166 | Interpretação, concordância, regência, crase, pontuação, acentuação |
| Informática | 66 | Segurança, Excel, Word, e-mail |
| Constitucional | 38 | Administração Pública (13), Poderes (10), federalismo (6) |
| **Perícia / saúde ocupacional** | **35** | Doenças ocupacionais, NRs, EPI, PAIR, CAT (18); laudo, perito, psiquiatria forense, Código de Ética (12); CID (2); nexo, capacidade, previdência (3) |
| Fora do edital | 1.331 | Clínica e especialidades (1.261), ética no serviço público (56), matemática (14) |

**O SUS é o bloco mais cobrado em todas as provas de médico.** Prioridade absoluta: Lei 8.080 e Atenção Básica.

## 2. Letra da correta: sem vício
- 4 alternativas: A 147 · B 144 · C 130 · D 147 (n = 568) → qui-quadrado 1,39, **p = 0,71**
- 5 alternativas: A 69 · B 56 · C 63 · D 66 · E 64 (n = 318) → qui-quadrado 1,47, **p = 0,83**
- V/F: 570 V (53%) × 507 F (47%)

**Chutar sempre a mesma letra não ajuda.** Nos itens de V/F há leve predominância de V.

## 3. Pistas de chute (múltipla escolha, n = 886; acaso ≈ 23%)
| Heurística | Todas | SUS + específicas (n=665) | Gerais (n=171) | **Só 5 alternativas (n=318, acaso 20%)** |
|---|---|---|---|---|
| **Mais integradora** (conectivos aditivos, sem absolutos) | **42%** (39–46%) | **44%** (40–48%) | 35% | **39%** (34–45%) |
| Menos palavras absolutas | 39% (36–42%) | 41% | 31% | 33% |
| Mais longa | 37% (34–40%) | 40% | 28% | 32% |
| Eliminar absolutos e sortear | 28% | 28% | 25% | 23% |
| Mais curta | 18%: **pior que o acaso** | 16% | 27% | 14% |

No formato da sua prova (5 alternativas), **a mais completa e equilibrada acerta 39%, quase o dobro do acaso**.
Em Português/Informática/Constituição as pistas quase não funcionam (28–35%): ali, só o conteúdo resolve.

**Palavras que praticamente nunca estão na correta** (886 corretas × 2.660 erradas):
| Palavra | Na correta | Nas erradas |
|---|---|---|
| exclusivamente | 0 | 88 |
| dispensa | 0 | 32 |
| suficiente | 0 | 16 |
| restringe | 0 | 15 |
| único | 0 | 11 |
| obrigatoriamente / unicamente | 0 | 7 / 6 |
| independentemente | 2 | 45 |
| sempre | 2 | 19 |
| todos | 5 | 51 |
| apenas | 129 (14,6%) | 572 (21,5%) — **não serve para eliminar** |

**Nos itens de V/F:** 30% dos itens FALSOS têm palavra absoluta, contra 15% dos VERDADEIROS. Absoluto no item
dobra a chance de ser falso, mas não decide sozinho.

## 4. Comando
CORRETA 88% · V/F ou sequência (dentro de múltipla escolha) 9% · afirmativas I-II-III 2% · **INCORRETA 0,5%**.

## 5. O que muda na sua estratégia
1. **SUS é o bloco decisivo**: 344 itens em 21 concursos. Lei 8.080 e APS/ESF somam 200.
2. **Elimine na hora** "exclusivamente", "dispensa", "suficiente", "restringe", "único".
3. **Na dúvida entre as restantes**, marque a mais completa e equilibrada (≈ 2× o acaso no formato A–E).
4. **Nunca marque a mais curta** por padrão.
5. **Perícia**: a banca cobra saúde do trabalhador (NRs, EPI, PAIR, CAT, riscos), laudo/perito e Código de Ética.
   Veja os 35 itens em `relatorio/pericia-igeduc.md`.

## Limitações
- Classificação de tema automática (regras de conteúdo) com revisão manual dos itens de perícia; os demais temas
  podem ter pequenos erros. As estatísticas de letra, pistas e palavras não dependem da classificação.
- Nenhum caderno de perito: a proporção de temas de perícia na sua prova segue o edital, não estas provas.
