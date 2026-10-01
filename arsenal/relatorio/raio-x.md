# Raio-X da banca IGEDUC

## Situação: etapas 1 a 3 bloqueadas neste ambiente (30/09–01/10/2026)

O ambiente de nuvem onde o arsenal foi construído bloqueia os domínios necessários à coleta:
`igeduc.org.br`, `igeduc.selecao.net.br`, `anexos.cdn.selecao.net.br`, `anexos-r2.selecao.net.br`,
`qconcursos.com`, `planalto.gov.br`, `in.gov.br`, `portal.cfm.org.br`. Sem os cadernos e gabaritos,
**nenhuma estatística real da banca foi calculada**. Nada abaixo é inventado.

### Como destravar (qualquer uma)
1. **Liberar a rede** do ambiente (menu do ambiente → Editar → Acesso à rede) para os domínios acima e
   pedir: "rode as etapas 1 a 3 do arsenal".
2. **Baixar à mão** e subir em `data/raw/`: cadernos de Médico/saúde nível superior + gabaritos definitivos.
   Ponto de partida confirmado: Japaratinga/AL 2025 → `https://igeduc.org.br/informacoes/95/`
   (caderno MEDICO CLINICO GERAL + gabarito). Varra também os IDs vizinhos (1–160) pela página da banca.
3. Usar o Claude in Chrome para baixar os PDFs de `igeduc.org.br/informacoes/<ID>/`.

## Hipóteses de estilo em uso (fornecidas pela Victoria, ~40 questões de 2026)
Fonte: Prefeituras de Salgueiro/PE e Paulo Afonso/BA. N ≈ 40, **não verificado por mim**.

| # | Hipótese | Uso no banco gerado |
|---|---|---|
| 1 | Nível superior = situacional longa, termina em "assinale a afirmativa CORRETA" | 71% situacionais em Perícia, 59% em SUS |
| 2 | Alternativas com tamanho e estrutura parecidos | Corrigido: a correta era a mais longa em 67%; agora 16% (≈ acaso de 20%) |
| 3 | Distratores = meia-verdade + palavra restritiva | Padrão principal dos distratores |
| 4 | A correta é a mais integradora | Usado com cautela (para não virar pista falsa) |
| 6 | Letras equilibradas (A=8, B=7, C=8, D=8, E=9) | Letras sorteadas: 18–22% cada |
| 7 | Pouca cobrança de número de artigo | Questões cobram o conceito aplicado; artigo só no comentário |

Com N = 40 e 5 letras, a hipótese 6 é compatível com distribuição uniforme (qui-quadrado ≈ 0,25, gl = 4,
p ≈ 0,99): **não há evidência de vício de letra**. Chutar sempre a mesma letra não ajuda.

## Estatística do próprio banco gerado (lote 1)
- 123 questões · letras A 22% / B 21% / C 20% / D 19% / E 18%
- Posição da correta no ranking de tamanho (1ª = mais longa): 16% / 14% / 22% / 28% / 20%
- Comando INCORRETA: 2% (meta 10–15%: corrigir nos próximos lotes)
