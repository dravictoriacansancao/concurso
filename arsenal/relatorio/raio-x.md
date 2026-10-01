# Raio-X da banca IGEDUC (provas reais)

Dados brutos: `relatorio/raio-x-dados.json` · Scripts: `coletar_historico.py` → `classificar_historico.py` → `raio_x.py`

## Amostra
| Concurso | Cadernos | Questões únicas |
|---|---|---|
| 95 · Japaratinga/AL 2025 | Médico Clínico Geral, Enfermeiro, Fisioterapeuta, Nutricionista, Psicólogo | 104 |
| 114 · São José do Seridó/RN 2025 | Médico, Farmacêutico/Bioquímico | 55 |
| 142 · Cabo de Santo Agostinho/PE 2026 | Médico do PSF, do Trabalho, Psiquiatra, Clínico Diarista, Enfermeiro do PSF, Farmacêutico | 33 |
| **Total** | **13 cadernos, 460 questões extraídas** | **192 únicas (188 válidas, 4 anuladas)** |

- Gabaritos: todos tirados do **gabarito definitivo oficial** de cada concurso, pelo bloco do cargo.
- Duplicatas: dentro de um concurso, cargos diferentes recebem as mesmas questões de conhecimentos gerais,
  **com a ordem das alternativas embaralhada**. Comparei o texto da alternativa correta em todas as cópias:
  nenhuma divergência. Cada questão foi contada uma vez.
- Em Cabo, todos os cadernos de saúde têm só conhecimentos gerais (Português, Constituição, ética, Informática).

## Formato
4 alternativas (A–D), 30 a 40 questões. **Porto Calvo terá 5 alternativas e 50 questões** (edital).

## 1. O que cai (dentro do edital do perito)
| Disciplina | Questões | Temas mais frequentes |
|---|---|---|
| Português | 29 | Interpretação (15), Sintaxe: concordância, regência, pontuação, colocação (11), Acentuação (3) |
| Informática | 27 | Segurança (9), Excel (8), Word (4), e-mail, redes sociais, hardware |
| Constitucional | 12 | Administração Pública (5, inclusive arts. 39 e 40), Poderes (2), direitos fundamentais (2) |
| SUS | 9 | Lei 8.080 (3, com artigo citado no enunciado), gestão municipal (2), APS/NASF (1); 3 fora do edital |
| Fora do edital | 115 | Específicas de cada cargo (106), ética no serviço público (9) |

No SUS, a banca **cita o artigo** no enunciado (Lei 8.080, art. 5º, I; art. 18, III) e usa afirmativas I-II-III.

## 2. Letra da correta: sem vício
A 53 · B 43 · C 41 · D 51 (n = 188). Qui-quadrado = 2,21, g.l. = 3, **p = 0,53**. Nenhum caderno isolado
mostrou vício (todos p > 0,1). **Chutar sempre a mesma letra não ajuda.**

## 3. Pistas de chute (acerto real; acaso = 25%)
| Heurística | Todas (n=188) | SUS + específicas de saúde (n=114) | Gerais (n=65) |
|---|---|---|---|
| Marcar a **mais integradora** (conectivos aditivos, sem absolutos) | **44%** (IC 37–51%) | 42% (33–51%) | 40% (29–52%) |
| Marcar a que tem **menos palavras absolutas** (empate → mais longa) | **42%** (35–49%) | 43% (34–52%) | 38% (28–51%) |
| Marcar a **mais longa** | **39%** (32–46%) | 43% (34–52%) | 35% (25–48%) |
| Eliminar as com absolutos e sortear entre as restantes | 32% (26–39%) | 33% (25–42%) | 27% (17–38%) |
| Marcar a mais curta | 19%: **pior que o acaso** | 13% | 23% |

Quando o enunciado pede **"a mais correta e completa"** (n = 19): menos absolutos 63%, mais longa 53%.

Com a amostra maior, as pistas ficaram **mais fracas do que na primeira análise** (com 106 questões, "menos
absolutos" em SUS/clínica dava 68%; agora 43%). Continuam bem acima do acaso, mas não substituem o estudo.

**Palavras que nunca apareceram na correta** (188 corretas × 564 erradas):
| Palavra | Na correta | Nas erradas |
|---|---|---|
| exclusivamente | 0 | 24 |
| sempre | 0 | 9 |
| suficiente | 0 | 8 |
| restringe | 0 | 6 |
| dispensa / somente | 0 | 3 cada |
| todos | 1 | 14 |
| apenas | 16 (8,5%) | 70 (12,4%) |

"apenas" aparece em 16 corretas: **não serve para eliminar**.

## 4. Comando
CORRETA 76% · **V/F ou sequência 18%** · afirmativas I-II-III 5% · INCORRETA/NÃO **0,5%**.
A banca praticamente não pede a incorreta. Treine questões de V/F: quase 1 em cada 5.

## 5. Estilo do enunciado
Enunciados longos e contextualizados; **caso concreto** (paciente, servidor, situação) em 17% (32/192),
concentrado nas específicas (24 de 106) e em Informática ("um assistente de tecnologia…").
Português, Constituição e SUS: praticamente só enunciado direto.

## 6. Repetição
Nenhuma questão repetida entre concursos diferentes. Dentro do concurso, conhecimentos gerais são
reaproveitados entre cargos com as alternativas embaralhadas.

## O que isso muda na sua estratégia
1. **Elimine na hora** alternativas com "exclusivamente", "sempre", "suficiente", "restringe", "dispensa".
2. **Na dúvida entre as restantes**, prefira a mais completa e equilibrada (≈ 40–44% contra 25%).
3. **Nunca chute a mais curta.**
4. **Prepare-se para V/F** (18% das questões) e para enunciados que citam artigo de lei no SUS.
5. **Treine com as 188 questões reais** no simulador (Treino → "Só provas reais IGEDUC" e Treino de chute).

## Limitações
3 concursos, 188 questões válidas. Nenhum caderno de perito. Os padrões de redação devem valer para a sua
prova (mesma banca, 2025–2026), mas a proporção de temas de perícia não pode ser estimada com estas provas.
