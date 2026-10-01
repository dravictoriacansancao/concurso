# Raio-X da banca IGEDUC (provas reais)

Dados brutos: `relatorio/raio-x-dados.json` · Script: `scripts/raio_x.py`

## Amostra
| Concurso | Cargo | Questões | Anuladas |
|---|---|---|---|
| 95 · Japaratinga/AL 2025 | Médico Clínico Geral | 40 | 1 |
| 114 · São José do Seridó/RN 2025 | Médico | 40 | 1 |
| 142 · Cabo de Santo Agostinho/PE 2026 | Médico do PSF, do Trabalho e Psiquiatra (**mesmo caderno**) | 30 | 2 |
| **Total** | | **110 únicas** (170 extraídas) | 4 |

Os 3 PDFs de Cabo têm gabarito idêntico letra por letra: é um caderno único de conhecimentos gerais aplicado
aos médicos. Foi contado uma vez só. Os 5 gabaritos foram conferidos contra o bloco oficial do PDF: 100% iguais.

**N = 106 questões válidas.** É uma amostra pequena: todos os percentuais abaixo trazem intervalo de confiança.

## Diferença de formato em relação à sua prova
Nestes concursos as questões têm **4 alternativas (A–D)** e 30 a 40 questões. O edital de Porto Calvo diz
**5 alternativas** e 50 questões. Esta é a mesma banca, mas com outro formato; o chute por acaso cai de 25% para 20%.

## 1. O que cai (questões dentro do edital do perito)
| Disciplina | Questões | Temas que mais apareceram |
|---|---|---|
| Português | 28 | Interpretação (14), Sintaxe: concordância, regência, pontuação, colocação (10), Acentuação (3) |
| Informática | 27 | Segurança (9: malware, ransomware, senhas, Wi-Fi/VPN, engenharia social), Excel (6), Word (4) |
| Constitucional | 10 | Administração Pública (3), Poderes (2), direitos fundamentais (2) |
| SUS | 9 | Lei 8.080 (3), gestão municipal (3), APS/NASF (1); 2 fora do edital (biossegurança, humanização) |
| Fora do edital | 36 | Clínica médica (30), ética no serviço público (6) |

No SUS, a banca cita **artigo de lei** no enunciado (Lei 8.080, art. 5º, I; art. 18, III). A hipótese
"poucas questões pedem artigo" não se confirmou no bloco SUS.

## 2. Letra da correta: sem vício
A 29 · B 22 · C 28 · D 27 (n = 106). Qui-quadrado = 1,09, g.l. = 3, **p = 0,78**. Também sem vício em
cada prova isolada (p = 0,29; 0,84; 0,92). **Chutar sempre a mesma letra não ajuda.**

## 3. Pistas que funcionam (taxa de acerto real vs acaso de 25%)
| Heurística | Todas (n=106) | SUS + clínica (n=38) | Gerais (n=62) |
|---|---|---|---|
| Marcar a **mais longa** | **43%** (IC 34–53%) | **58%** (42–72%) | 39% (28–51%) |
| Marcar a que tem **menos palavras absolutas** (empate → mais longa) | **48%** (39–58%) | **68%** (53–81%) | 36% (25–48%) |
| Marcar a **mais integradora** (conectivos aditivos, sem absolutos) | **52%** (43–61%) | **66%** (50–79%) | 40% (29–53%) |
| Eliminar as com absolutos e sortear entre as restantes | 33% (25–42%) | 41% (26–55%) | 27% (18–40%) |
| Marcar a mais curta | 18% (12–26%): **pior que o acaso** | 10% | 18% |

Quando o enunciado pede **"a mais correta e completa"** (n = 16): mais longa 62%, menos absolutos 69%.

**Palavras que nunca apareceram na correta** (n = 106 corretas × 318 erradas):
| Palavra | Na correta | Nas erradas |
|---|---|---|
| exclusivamente | 0 | 14 |
| sempre | 0 | 8 |
| restringe / suficiente | 0 | 5 cada |
| dispensa / somente | 0 | 3 cada |
| todos | 1 | 10 |
| apenas | 8 (7,5%) | 41 (12,9%) |

"apenas" aparece na correta: não serve sozinho para eliminar.

## 4. Comando da questão
CORRETA 83% · V/F ou sequência 13% · afirmativas I-II-III 7% · INCORRETA/NÃO **1%**.
A banca quase nunca pede a incorreta. Questões V/F e de "afirmativas I, II, III" aparecem no bloco SUS.

## 5. Estilo do enunciado
Enunciados longos e contextualizados ("A Constituição estabelece… Considerando…"), mas quase nunca um **caso
concreto**: só 13 de 110 descrevem uma situação com pessoa/paciente. A hipótese "nível superior = situacional"
se confirmou como "contextual", não como "caso clínico".

## 6. Repetição entre provas
Nenhuma questão repetida (similaridade > 0,8) entre concursos diferentes. Dentro de um mesmo concurso,
o caderno de conhecimentos gerais é **reaproveitado entre cargos**.

## O que isso muda na sua estratégia
1. **No chute de SUS e de perícia:** prefira a alternativa mais completa e sem absolutos (≈ 2,5× o acaso).
2. **Elimine na hora** qualquer alternativa com "exclusivamente", "sempre", "suficiente", "dispensa", "restringe".
3. **Não confie no chute em Português e Informática** (≈ 36–40%): ali, estude o conteúdo.
4. **Treine com as 106 questões reais** no simulador (Treino → "Só provas reais IGEDUC" e Treino de chute).

## Limitações
Amostra de 3 concursos e 106 questões. Cargos de médico generalista, não de perito. Os padrões de
distratores devem valer para a sua prova (mesma banca, mesmo ano), mas a proporção de temas de perícia
não pode ser estimada com estas provas: elas não têm bloco de perícia.
