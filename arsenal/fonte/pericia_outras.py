"""Inéditas no estilo IGEDUC (A–E) sobre os temas que as OUTRAS bancas mais cobraram em prova de perito
(raio-X em relatorio/outras-bancas.md): NR 7/PCMSO, insalubridade, PGR, NR 32, telemarketing, pneumoconioses,
Schilling, qualidade de segurado, reaquisição de carência, estabilidade acidentária, auxílio-acidente por perda
auditiva, BPC, isenção de IR e Código de Ética Médica na perícia. Fatos ancorados nos gabaritos oficiais
quando o tema apareceu nas provas (FGV, UFG, Cebraspe)."""
from _base import q

Q = []
D = "Perícia"
SIT, DIR = "situacional", "direto"
C, I = "CORRETA", "INCORRETA"
OCUP = "Doenças ocupacionais e relacionadas ao trabalho"
PREV = "Perícia médica previdenciária"
BIO = "Bioética aplicada à perícia médica"
CAP = "Avaliação da capacidade laborativa"

# ---------------------------------------------------------------- NR 7 / PCMSO
q(Q, D, OCUP, "NR 7 – exame demissional", 3, SIT, C,
  "Sandra e Dionísio trabalham em empresas diferentes e fizeram o último exame clínico ocupacional há 100 dias. "
  "A empresa de Sandra é de grau de risco 3; a de Dionísio, de grau de risco 2. Ambos serão desligados nesta "
  "semana. Considerando a NR 7, assinale a afirmativa CORRETA.",
  "Dionísio pode ter o exame demissional dispensado, pois o último exame foi feito há menos de 135 dias.",
  [("Sandra pode ter o exame demissional dispensado, pois o último exame foi feito há menos de 135 dias.",
    "Para graus de risco 3 e 4 o prazo de dispensa é de 90 dias; 100 dias já o ultrapassa."),
   ("Ambos podem ter o exame demissional dispensado, pois o último exame foi feito há menos de 180 dias.",
    "Os prazos da NR 7 são 135 dias (graus 1 e 2) e 90 dias (graus 3 e 4); não existe prazo de 180 dias."),
   ("Nenhum dos dois pode ter o exame dispensado, pois o demissional é obrigatório em qualquer situação.",
    "A NR 7 admite a dispensa quando o exame mais recente está dentro do prazo do grau de risco."),
   ("Ambos devem repetir o exame, que deve ser feito em até 30 dias após o término do contrato.",
    "O demissional deve ser feito em até 10 dias contados do término do contrato.")],
  "NR 7: o exame demissional deve ser feito em até 10 dias do término do contrato e pode ser dispensado se o exame clínico ocupacional mais recente tiver menos de 135 dias (graus de risco 1 e 2) ou menos de 90 dias (graus 3 e 4). Questão inspirada na FGV/Macaé 2024 (gabarito: dispensa só para Dionísio).",
  "NR 7 (exame clínico demissional)", "Inverter os prazos: o grau de risco MAIOR tem o prazo MENOR (90 dias).")

q(Q, D, OCUP, "NR 7 – exame de retorno", 2, SIT, C,
  "Um auxiliar administrativo ficou 45 dias afastado por fratura sofrida em acidente doméstico, sem relação "
  "com o trabalho, e vai reassumir a função. Considerando a NR 7, assinale a afirmativa CORRETA.",
  "Ele deve fazer o exame de retorno antes de reassumir a função, e o médico deve definir se o retorno será gradativo.",
  [("Ele fica dispensado do exame de retorno, pois este só é exigido após afastamento por doença ocupacional.",
    "O exame de retorno é exigido após ausência de 30 dias ou mais por doença ou acidente, ocupacional ou não."),
   ("Ele deve fazer o exame de retorno em até 30 dias após reassumir a função, conforme a agenda do PCMSO.",
    "O exame deve ser feito ANTES de o empregado reassumir as funções."),
   ("Ele deve fazer novo exame admissional, pois o afastamento superior a 30 dias suspende o contrato de trabalho.",
    "Não há novo admissional; o exame previsto é o de retorno ao trabalho."),
   ("Ele só fará exame de retorno se o afastamento tiver ultrapassado 60 dias, prazo fixado pela NR 7.",
    "O prazo da NR 7 é de 30 dias ou mais, não 60.")],
  "NR 7: o exame de retorno deve ser realizado antes que o empregado reassuma as funções quando ausente por 30 dias ou mais por doença ou acidente, de natureza ocupacional ou não. Na avaliação, o médico define a necessidade de retorno gradativo (gabarito Cebraspe/MPS 2025, item 80: Certo).",
  "NR 7 (exame de retorno ao trabalho)", "Achar que o retorno só vale para doença ocupacional.")

q(Q, D, OCUP, "NR 7 – audiometria", 2, DIR, C,
  "Segundo a NR 7, no controle médico de trabalhadores expostos a níveis de pressão sonora elevados, a "
  "periodicidade mínima do exame audiométrico é:",
  "Na admissão, anualmente e na demissão.",
  [("Na admissão e na demissão, apenas.",
    "Falta o exame anual, que é obrigatório durante a exposição."),
   ("Na admissão e a cada dois anos durante a exposição.",
    "A periodicidade é anual, não bienal."),
   ("Somente quando o trabalhador relatar queixa auditiva.",
    "O controle é sistemático, não dependente de queixa."),
   ("Na admissão, a cada cinco anos e na demissão.",
    "Não existe periodicidade quinquenal na NR 7.")],
  "NR 7, Anexo II: a audiometria deve ser feita, no mínimo, na admissão, anualmente e na demissão (gabarito FGV/Macaé 2024, questão 55).",
  "NR 7, Anexo II (Controle médico ocupacional da exposição a níveis de pressão sonora elevados)",
  "Confundir a audiometria anual com a periodicidade bienal do exame clínico dos demais empregados.")

q(Q, D, OCUP, "NR 7 – ASO e sigilo", 2, DIR, I,
  "Sobre o Atestado de Saúde Ocupacional (ASO) e o PCMSO, conforme a NR 7, assinale a alternativa INCORRETA.",
  "O ASO deve informar o diagnóstico do trabalhador pela CID, para que o empregador possa organizar a função.",
  [("O ASO deve conter a definição de apto ou inapto para a função específica que o empregado exerce.",
    "Correta: é conteúdo obrigatório do ASO."),
   ("O ASO deve indicar os exames realizados e as datas em que foram feitos.",
    "Correta: é conteúdo obrigatório do ASO."),
   ("O ASO deve trazer o nome e o número de registro profissional do médico que fez o exame clínico.",
    "Correta: é conteúdo obrigatório do ASO."),
   ("O PCMSO tem por objetivo proteger e preservar a saúde dos empregados em relação aos riscos ocupacionais.",
    "Correta: é o objetivo do PCMSO.")],
  "O ASO informa aptidão ou inaptidão, riscos, exames e médico responsável. O diagnóstico é protegido pelo sigilo médico e não vai ao empregador (CEM, art. 76).",
  "NR 7 (conteúdo do ASO); CEM, art. 76", "Confundir aptidão (que vai ao empregador) com diagnóstico (que é sigiloso).")

# ---------------------------------------------------------------- Insalubridade / NR 15
q(Q, D, OCUP, "NR 15 – graus e adicional", 2, DIR, C,
  "Conforme a NR 15, a exposição acima do limite de tolerância às radiações ionizantes e ao calor caracteriza, "
  "respectivamente, insalubridade de grau:",
  "máximo e médio.",
  [("médio e máximo.", "Inverte os graus: radiação ionizante é grau máximo; calor, grau médio."),
   ("máximo e máximo.", "O calor é grau médio."),
   ("mínimo e médio.", "Radiação ionizante é grau máximo."),
   ("médio e mínimo.", "Radiação ionizante é grau máximo; calor, grau médio.")],
  "NR 15: radiações ionizantes (Anexo 5) geram insalubridade de grau máximo (adicional de 40% sobre o salário mínimo); calor (Anexo 3), grau médio (20%). Gabaritos UFG/Goiânia 2022, questões 36 e 37.",
  "NR 15, Anexos 3 e 5; item 15.2", "Os percentuais: máximo 40%, médio 20%, mínimo 10%.")

q(Q, D, OCUP, "NR 15 – critério quantitativo × qualitativo", 3, DIR, C,
  "Na caracterização da insalubridade pela NR 15, alguns agentes são avaliados por limite de tolerância "
  "(critério quantitativo) e outros por inspeção no local de trabalho (critério qualitativo). Assinale a "
  "alternativa que apresenta, respectivamente, um agente quantitativo e um qualitativo.",
  "Vibração e umidade.",
  [("Umidade e ruído contínuo.", "Inverte: umidade é qualitativa; ruído é quantitativo."),
   ("Frio e calor.", "Frio é qualitativo e calor é quantitativo: a ordem está invertida."),
   ("Agentes biológicos e radiação ionizante.", "Biológicos são qualitativos; radiação ionizante é quantitativa."),
   ("Umidade e agentes biológicos.", "Os dois são qualitativos.")],
  "Quantitativos: ruído, calor, radiações ionizantes, vibração, poeiras minerais e os agentes químicos do Anexo 11. Qualitativos: radiações não ionizantes, frio, umidade, agentes químicos do Anexo 13 e biológicos (Anexo 14). Gabaritos UFG/Goiânia 2022, questões 38 e 39.",
  "NR 15, Anexos 1 a 14", "Frio e umidade parecem mensuráveis, mas são avaliados por inspeção.")

q(Q, D, OCUP, "NR 15 – ruído", 2, DIR, C,
  "Pela NR 15, o limite de tolerância para ruído contínuo ou intermitente de 85 dB(A) permite exposição diária "
  "máxima de:",
  "8 horas.",
  [("4 horas.", "4 horas é o limite para 90 dB(A)."),
   ("6 horas.", "6 horas corresponde a 87 dB(A)."),
   ("2 horas.", "2 horas é o limite para 95 dB(A)."),
   ("12 horas.", "A tabela da NR 15 começa em 85 dB(A) com 8 horas; não prevê 12 horas.")],
  "NR 15, Anexo 1: 85 dB(A) → 8 h; cada aumento de 5 dB reduz pela metade o tempo (90 → 4 h; 95 → 2 h; 100 → 1 h). Não é permitida exposição acima de 115 dB(A) sem proteção adequada. Gabarito UFG/Goiânia 2022, questão 49.",
  "NR 15, Anexo 1", "Errar a regra de dobra: cada +5 dB(A) corta o tempo pela metade.")

q(Q, D, OCUP, "Insalubridade – vários agentes", 3, SIT, C,
  "Um trabalhador de fundição fica exposto acima dos limites a ruído (grau médio) e a poeira mineral de "
  "sílica (grau máximo). Sobre o adicional de insalubridade, assinale a afirmativa CORRETA.",
  "Recebe apenas o adicional do grau mais elevado, pois os adicionais não se somam.",
  [("Recebe a soma dos dois adicionais, pois cada agente gera direito autônomo.",
    "A NR 15 manda considerar só o grau mais elevado, vedada a percepção cumulativa."),
   ("Recebe apenas o adicional do grau médio, pois o ruído é o agente avaliado primeiro.",
    "Prevalece o grau mais elevado, e não a ordem de avaliação."),
   ("Recebe a média dos dois adicionais, calculada sobre o salário contratual.",
    "Não existe média: vale o grau mais elevado, calculado sobre o salário mínimo."),
   ("Não recebe adicional se usar EPI, ainda que o equipamento não neutralize a exposição.",
    "Só a eliminação ou neutralização da insalubridade afasta o adicional; EPI ineficaz não basta.")],
  "NR 15, item 15.3: havendo mais de um fator de insalubridade, considera-se apenas o de grau mais elevado para o adicional, vedada a percepção cumulativa. O adicional cessa com a eliminação ou neutralização do risco (item 15.4).",
  "NR 15, itens 15.2 a 15.4", "Somar adicionais de agentes diferentes.")

# ---------------------------------------------------------------- PGR / NR 1, NR 32, NR 17
q(Q, D, OCUP, "NR 1 – PGR", 2, DIR, C,
  "Conforme a NR 1, o Programa de Gerenciamento de Riscos (PGR) deve conter, no mínimo, os seguintes "
  "documentos:",
  "o inventário de riscos e o plano de ação.",
  [("o PCMSO e o laudo de insalubridade.",
    "O PCMSO é programa da NR 7, e o laudo de insalubridade não integra o PGR."),
   ("a CAT e o mapa de riscos da CIPA.",
    "A CAT comunica acidente; o mapa de riscos é da CIPA. Nenhum é documento mínimo do PGR."),
   ("o inventário de riscos e o ASO de cada empregado.",
    "O ASO é documento do PCMSO, não do PGR."),
   ("o plano de ação e a ficha de entrega de EPI.",
    "Falta o inventário de riscos; a ficha de EPI não é documento mínimo do PGR.")],
  "NR 1: o PGR deve conter, no mínimo, inventário de riscos e plano de ação. O PCMSO (NR 7) deve estar articulado com os riscos do PGR.",
  "NR 1, item 1.5.7.1", "Confundir os documentos do PGR (NR 1) com os do PCMSO (NR 7).")

q(Q, D, OCUP, "NR 32 – serviços de saúde", 2, DIR, I,
  "Sobre as medidas de proteção da NR 32, que trata da segurança e saúde no trabalho em serviços de saúde, "
  "assinale a alternativa INCORRETA.",
  "É permitido reencapar agulhas usadas quando o trabalhador usar luvas de procedimento.",
  [("É vedado o uso de calçados abertos pelos trabalhadores expostos a agentes biológicos.",
    "Correta: vedação expressa da NR 32."),
   ("É vedado o uso de adornos nos postos de trabalho com exposição a agentes biológicos.",
    "Correta: vedação expressa da NR 32."),
   ("O empregador deve oferecer gratuitamente vacinação contra tétano, difteria e hepatite B.",
    "Correta: obrigação expressa da NR 32."),
   ("É vedado consumir alimentos e bebidas nos postos de trabalho com exposição a agentes biológicos.",
    "Correta: vedação expressa da NR 32.")],
  "A NR 32 veda o reencape e a desconexão manual de agulhas em qualquer situação; luva não autoriza o reencape.",
  "NR 32 (agentes biológicos: vedações, perfurocortantes e vacinação)", "Achar que o EPI torna aceitável uma prática que a norma veda.")

q(Q, D, OCUP, "NR 17 – telemarketing", 2, DIR, C,
  "Conforme o anexo da NR 17 sobre trabalho em teleatendimento/telemarketing, o tempo de trabalho em efetiva "
  "atividade de atendimento, nele incluídas as pausas e sem prejuízo da remuneração, é de, no máximo:",
  "6 horas diárias.",
  [("8 horas diárias, com duas pausas de 10 minutos.", "O limite do anexo é de 6 horas, já incluídas as pausas."),
   ("4 horas diárias.", "O limite é de 6 horas."),
   ("7 horas diárias, sem pausas obrigatórias.", "O limite é de 6 horas e há pausas obrigatórias."),
   ("44 horas semanais, distribuídas livremente.", "O anexo limita o tempo diário a 6 horas.")],
  "NR 17, anexo de teleatendimento: máximo de 6 horas diárias de efetiva atividade, incluídas as pausas; duas pausas de 10 minutos contínuos e intervalo de 20 minutos para repouso e alimentação. Gabarito UFG/Goiânia 2022, questão 48.",
  "NR 17, Anexo II", "Aplicar a jornada geral de 8 horas a uma atividade com limite especial.")

# ---------------------------------------------------------------- Nexo, Schilling, pneumoconioses, saúde mental
q(Q, D, "Avaliação de dano corporal e nexo causal", "Classificação de Schilling", 3, DIR, C,
  "Na classificação de Schilling das doenças relacionadas ao trabalho, assinale a alternativa que associa "
  "CORRETAMENTE o grupo ao exemplo.",
  "Grupo I (trabalho como causa necessária): silicose e intoxicação por chumbo.",
  [("Grupo I (trabalho como causa necessária): doença coronariana e varizes de membros inferiores.",
    "Coronariopatia e varizes são do grupo II: o trabalho contribui, mas não é necessário."),
   ("Grupo II (trabalho como fator contributivo): silicose e asbestose.",
    "Silicose e asbestose são do grupo I: sem a exposição ocupacional, não ocorrem."),
   ("Grupo III (trabalho como provocador ou agravante): intoxicação por chumbo e silicose.",
    "São do grupo I."),
   ("Grupo III (trabalho como provocador ou agravante): câncer de pulmão em trabalhador exposto ao asbesto.",
    "O câncer é exemplo clássico do grupo II.")],
  "Schilling: I – trabalho como causa necessária (doenças profissionais clássicas: silicose, saturnismo); II – fator contributivo, não necessário (coronariopatia, varizes, cânceres); III – provocador de distúrbio latente ou agravador de doença estabelecida (asma, dermatite de contato alérgica, transtornos mentais).",
  "Ministério da Saúde, Doenças relacionadas ao trabalho: manual de procedimentos (2001)",
  "Pôr no grupo III doenças que só existem com a exposição ocupacional.")

q(Q, D, "Avaliação pericial em doenças respiratórias", "Pneumoconioses", 3, DIR, C,
  "Sobre as pneumoconioses e a avaliação das doenças respiratórias ocupacionais, assinale a afirmativa CORRETA.",
  "A radiografia de tórax pela classificação da OIT é o exame de referência para rastrear silicose e asbestose.",
  [("A asma ocupacional é uma pneumoconiose, e o exame mais indicado para o diagnóstico é a radiografia de tórax.",
    "Asma ocupacional não é pneumoconiose; o diagnóstico é funcional (espirometria, pico de fluxo seriado)."),
   ("A silicose acomete preferencialmente os lobos inferiores, enquanto a asbestose predomina nos lobos superiores.",
    "É o contrário: silicose nos lobos superiores; asbestose nas bases."),
   ("A espirometria normal descarta pneumoconiose, dispensando a radiografia de tórax.",
    "Doença radiológica inicial pode ter espirometria normal."),
   ("A asbestose cessa a progressão com o afastamento da exposição, o que dispensa acompanhamento.",
    "As pneumoconioses fibrogênicas podem progredir mesmo após o fim da exposição.")],
  "Pneumoconiose = doença pulmonar por deposição de poeira com reação tecidual. A radiografia de tórax padronizada pela OIT é a referência para rastreio e vigilância; a espirometria avalia o prejuízo funcional. A Cebraspe (MPS 2025, item 68) considerou ERRADO chamar a asma ocupacional de pneumoconiose.",
  "Classificação Internacional de Radiografias de Pneumoconioses (OIT); NR 7, Anexo III",
  "Pôr a asma ocupacional entre as pneumoconioses.")

q(Q, D, "Avaliação pericial em doenças psiquiátricas", "TEPT – latência", 3, DIR, C,
  "Sobre o transtorno de estresse pós-traumático (TEPT) na avaliação de trabalhador vítima de assalto em "
  "serviço, assinale a afirmativa CORRETA.",
  "Os sintomas podem surgir após um período de latência de semanas a meses depois do evento traumático.",
  [("Os sintomas surgem obrigatoriamente logo após o trauma, sem período de latência.",
    "O TEPT costuma surgir após latência variável; a Cebraspe (MPS 2025, item 67) julgou isso ERRADO."),
   ("O diagnóstico dispensa a exposição a evento traumático quando há sintomas de revivescência.",
    "A exposição a evento traumático é critério essencial."),
   ("O TEPT impede o nexo com o trabalho quando o evento ocorre no trajeto ou fora do posto de trabalho.",
    "Evento em serviço ou equiparado a acidente do trabalho admite nexo."),
   ("A presença de revivescências é suficiente, por si só, para concluir pela incapacidade laboral permanente.",
    "Diagnóstico não é sinônimo de incapacidade, menos ainda permanente.")],
  "CID-10 F43.1: o TEPT surge como resposta tardia ou protraída a evento traumático, com latência que pode ir de semanas a meses (raramente mais de 6 meses). Cursa com revivescências, evitação, embotamento e hiperexcitação.",
  "CID-10 F43.1 (OMS)", "Exigir início imediato; o 'pós' indica resposta tardia.")

# ---------------------------------------------------------------- Previdenciária
q(Q, D, PREV, "Qualidade de segurado – período de graça", 3, SIT, C,
  "Um segurado empregado, com 8 anos de contribuição ininterrupta ao RGPS, foi demitido e não voltou a contribuir. "
  "Considerando o art. 15 da Lei nº 8.213/1991, assinale a afirmativa CORRETA.",
  "Mantém a qualidade de segurado por até 12 meses, prazo acrescido de 12 meses se comprovar o desemprego.",
  [("Mantém a qualidade de segurado por até 24 meses, porque já pagou mais de 120 contribuições.",
    "8 anos são 96 contribuições; a prorrogação para 24 meses exige mais de 120 contribuições sem perda da qualidade."),
   ("Perde a qualidade de segurado no mês seguinte ao da última contribuição.",
    "O art. 15 assegura o período de graça."),
   ("Mantém a qualidade de segurado sem limite de prazo, por ter contribuído mais de 5 anos.",
    "Sem limite de prazo, só quem está em gozo de benefício (exceto o auxílio-acidente)."),
   ("Mantém a qualidade de segurado por apenas 6 meses, prazo próprio do segurado facultativo.",
    "6 meses é o prazo do facultativo; o empregado tem 12 meses.")],
  "Art. 15: até 12 meses após cessarem as contribuições (II), prorrogáveis para 24 meses se já pagou mais de 120 contribuições sem perder a qualidade (§ 1º) e acrescidos de 12 meses para o desempregado que comprovar a situação (§ 2º). O facultativo tem 6 meses (VI).",
  "Lei 8.213/1991, art. 15", "Contar anos como se fossem mais de 120 contribuições.")

q(Q, D, PREV, "Qualidade de segurado – sem limite de prazo", 2, DIR, I,
  "Sobre a manutenção da qualidade de segurado do RGPS, assinale a alternativa INCORRETA.",
  "Mantém a qualidade de segurado, sem limite de prazo, quem recebe o benefício de prestação continuada (BPC/LOAS).",
  [("Mantém a qualidade de segurado, sem limite de prazo, quem está em gozo de auxílio por incapacidade temporária.",
    "Correta: art. 15, I."),
   ("O segurado facultativo mantém a qualidade de segurado por até 6 meses após cessar as contribuições.",
    "Correta: art. 15, VI."),
   ("O segurado acometido de doença de segregação compulsória mantém a qualidade por até 12 meses após cessar a segregação.",
    "Correta: art. 15, III."),
   ("O período de graça do empregado pode ser acrescido de 12 meses se ele comprovar o desemprego.",
    "Correta: art. 15, § 2º.")],
  "O BPC/LOAS é benefício assistencial, não previdenciário: não mantém a qualidade de segurado. Sem limite de prazo, só quem está em gozo de benefício previdenciário, exceto o auxílio-acidente (art. 15, I). Cebraspe (MPS 2025, item 93) julgou ERRADO incluir o BPC.",
  "Lei 8.213/1991, art. 15; Lei 8.742/1993, art. 20", "Tratar o BPC (assistência) como benefício previdenciário.")

q(Q, D, PREV, "Reaquisição de carência", 3, SIT, C,
  "Segurado que perdeu a qualidade de segurado volta a contribuir e, meses depois, fica incapaz por "
  "lombociatalgia, doença que não isenta de carência. Considerando o art. 27-A da Lei nº 8.213/1991, para "
  "aproveitar as contribuições anteriores ao auxílio por incapacidade temporária ele precisa contar, a partir "
  "da nova filiação, com:",
  "6 contribuições mensais, metade da carência exigida.",
  [("12 contribuições mensais, a carência integral exigida.",
    "O art. 27-A exige metade da carência para aproveitar as contribuições anteriores."),
   ("4 contribuições mensais, um terço da carência exigida.",
    "A regra de um terço foi substituída pela metade (Lei 13.846/2019)."),
   ("nenhuma contribuição, pois as contribuições anteriores são computadas de imediato.",
    "Após a perda da qualidade, é preciso cumprir metade da carência para reaproveitá-las."),
   ("24 contribuições mensais, o dobro da carência, como penalidade pela perda da qualidade.",
    "Não há regra de dobro; a lei exige metade.")],
  "Art. 27-A: perdida a qualidade de segurado, para auxílio por incapacidade temporária, aposentadoria por incapacidade permanente, salário-maternidade e auxílio-reclusão o segurado deve contar, a partir da nova filiação, com metade da carência. Para o auxílio (carência de 12), são 6. Gabarito Cebraspe MPS 2025, item 95: Certo.",
  "Lei 8.213/1991, arts. 25, I, e 27-A", "Lembrar a regra antiga de um terço.")

q(Q, D, PREV, "Estabilidade acidentária", 2, DIR, C,
  "Sobre a garantia de emprego do segurado que sofreu acidente do trabalho, prevista no art. 118 da Lei nº "
  "8.213/1991, assinale a afirmativa CORRETA.",
  "A garantia é de, no mínimo, 12 meses após cessar o auxílio-doença acidentário, independentemente de auxílio-acidente.",
  [("A garantia é de, no máximo, 12 meses após cessar o auxílio-doença acidentário.",
    "A lei fala em prazo MÍNIMO de 12 meses; a Cebraspe (MPS 2025, item 82) julgou 'máximo' ERRADO."),
   ("A garantia depende de o segurado passar a receber auxílio-acidente após a alta.",
    "A garantia independe de auxílio-acidente (Cebraspe MPS 2025, item 81: Certo)."),
   ("A garantia começa na data do acidente e dura 12 meses, mesmo sem afastamento previdenciário.",
    "O prazo conta da cessação do auxílio-doença acidentário."),
   ("A garantia alcança qualquer afastamento previdenciário, ainda que a doença não tenha relação com o trabalho.",
    "A garantia é do acidentado do trabalho (ou doença ocupacional equiparada).")],
  "Art. 118: o segurado que sofreu acidente do trabalho tem garantida, pelo prazo mínimo de 12 meses, a manutenção do contrato após a cessação do auxílio-doença acidentário, independentemente de percepção de auxílio-acidente.",
  "Lei 8.213/1991, art. 118", "Trocar 'mínimo' por 'máximo'.")

q(Q, D, PREV, "Auxílio-acidente – perda auditiva", 3, SIT, C,
  "Metalúrgico com PAIR leve e bilateral, de nexo ocupacional reconhecido, continua exercendo a mesma função "
  "sem limitação comprovada. Ele requer auxílio-acidente. Considerando a Lei nº 8.213/1991, assinale a "
  "afirmativa CORRETA.",
  "Não faz jus ao benefício, pois a perda auditiva só gera auxílio-acidente se reduzir a capacidade para o trabalho habitual.",
  [("Faz jus ao benefício, pois qualquer grau de perda auditiva ocupacional gera auxílio-acidente.",
    "A perda auditiva em qualquer grau só gera o benefício se houver redução comprovada da capacidade."),
   ("Faz jus ao benefício, pois basta o nexo causal reconhecido, dispensando avaliação da capacidade.",
    "A lei exige nexo E redução ou perda da capacidade."),
   ("Não faz jus ao benefício, pois a PAIR é doença degenerativa e não é considerada doença do trabalho.",
    "A PAIR por ruído ocupacional é doença relacionada ao trabalho."),
   ("Não faz jus ao benefício, pois o auxílio-acidente exige perda auditiva total e bilateral.",
    "A lei não exige perda total; exige redução da capacidade para o trabalho habitual.")],
  "Art. 86, § 4º: a perda da audição, em qualquer grau, só gera auxílio-acidente quando, além do nexo com o trabalho, resultar comprovadamente em redução ou perda da capacidade para o trabalho habitual. Gabarito Cebraspe MPS 2025, item 100: Certo.",
  "Lei 8.213/1991, art. 86, § 4º", "Achar que nexo reconhecido basta.")

q(Q, D, PREV, "BPC – revisão e acumulação", 2, DIR, C,
  "Sobre o benefício de prestação continuada (BPC) da Lei nº 8.742/1993 (LOAS), assinale a afirmativa CORRETA.",
  "Deve ser revisto a cada 2 anos para avaliar a continuidade das condições que lhe deram origem.",
  [("Pode ser acumulado com aposentadoria do RGPS, desde que a renda familiar permaneça baixa.",
    "É vedada a acumulação com outro benefício da seguridade, salvo assistência médica e pensão especial indenizatória."),
   ("Exige carência de 12 contribuições e qualidade de segurado na data do requerimento.",
    "É benefício assistencial: não exige contribuição nem qualidade de segurado."),
   ("Exige incapacidade para o trabalho igual à do auxílio por incapacidade temporária.",
    "Exige deficiência com impedimento de longo prazo (2 anos ou mais), em avaliação biopsicossocial; Cebraspe MPS 2025, item 99: Errado."),
   ("Gera pensão por morte aos dependentes do beneficiário falecido.",
    "O BPC é personalíssimo e não gera pensão.")],
  "LOAS, art. 21: o BPC deve ser revisto a cada 2 anos. Art. 20, § 4º: não pode ser acumulado com outro benefício da seguridade social, salvo assistência médica e pensão especial indenizatória. Deficiência = impedimento de longo prazo, mínimo de 2 anos (art. 20, §§ 2º e 10).",
  "Lei 8.742/1993, arts. 20 e 21", "Aplicar regras previdenciárias (carência, pensão) a benefício assistencial.")

q(Q, D, "Avaliação de invalidez e incapacidade permanente", "Isenção de IR – doença grave", 3, SIT, C,
  "Servidor ativo, em plena atividade, tem diagnóstico de neoplasia maligna em tratamento e pede ao perito "
  "laudo para isenção do imposto de renda prevista na Lei nº 7.713/1988 (art. 6º, XIV). Assinale a afirmativa "
  "CORRETA.",
  "A isenção alcança proventos de aposentadoria, reforma ou pensão, e não a remuneração da atividade.",
  [("A isenção alcança a remuneração do servidor ativo, bastando o laudo de doença grave.",
    "O inciso XIV isenta proventos de aposentadoria, reforma e pensão, não a remuneração da ativa."),
   ("A isenção exige que a neoplasia tenha relação com o trabalho, por se tratar de moléstia profissional.",
    "Neoplasia maligna está listada à parte; não precisa ser ocupacional."),
   ("A isenção exige incapacidade total e permanente para qualquer trabalho.",
    "Basta a doença listada; não se exige incapacidade."),
   ("A isenção vale para qualquer doença crônica, a critério do perito, desde que haja tratamento contínuo.",
    "O rol da lei é taxativo.")],
  "Lei 7.713/1988, art. 6º, XIV: isentos os proventos de aposentadoria ou reforma (e pensão) recebidos por portadores das doenças listadas (moléstia profissional, tuberculose ativa, alienação mental, esclerose múltipla, neoplasia maligna, cegueira, hanseníase, paralisia irreversível e incapacitante, cardiopatia grave, Parkinson, espondiloartrose anquilosante, nefropatia grave, hepatopatia grave, Paget avançado, contaminação por radiação, AIDS, fibrose cística). O rol é taxativo.",
  "Lei 7.713/1988, art. 6º, XIV", "Achar que a isenção vale para o salário da ativa.")

# ---------------------------------------------------------------- Ética na perícia
q(Q, D, BIO, "CEM – sigilo em exame ocupacional", 2, SIT, C,
  "O gerente de uma empresa pede ao médico do trabalho o diagnóstico que motivou o atestado de um empregado, "
  "alegando necessidade de 'planejar a equipe'. Não há risco à saúde de outros empregados nem da comunidade. "
  "Conforme o Código de Ética Médica, assinale a afirmativa CORRETA.",
  "O médico não deve revelar o diagnóstico, pois a exigência da empresa não afasta o sigilo.",
  [("O médico deve revelar o diagnóstico, pois foi contratado pela empresa e a ela deve lealdade.",
    "O art. 76 veda revelar informações de exames de trabalhadores, inclusive por exigência dos dirigentes."),
   ("O médico pode revelar o diagnóstico se o gerente assinar termo de confidencialidade.",
    "Termo de terceiro não substitui justa causa, dever legal ou consentimento escrito do paciente."),
   ("O médico deve revelar apenas o código da CID, que não identifica a doença para leigos.",
    "A CID identifica o diagnóstico e também está protegida pelo sigilo."),
   ("O médico pode revelar o diagnóstico verbalmente, desde que não o registre por escrito.",
    "O sigilo vale para qualquer forma de revelação.")],
  "CEM, art. 76: é vedado revelar informações confidenciais obtidas em exames médicos de trabalhadores, inclusive por exigência dos dirigentes de empresas, salvo se o silêncio puser em risco a saúde dos empregados ou da comunidade. Art. 73: sigilo, salvo motivo justo, dever legal ou consentimento por escrito do paciente.",
  "Resolução CFM 2.217/2018 (CEM), arts. 73 e 76", "Achar que o vínculo com a empresa autoriza a revelação.")

q(Q, D, BIO, "CEM – remuneração do perito", 2, DIR, I,
  "Considerando as vedações do Código de Ética Médica ao médico que atua como perito ou auditor, assinale a "
  "alternativa INCORRETA.",
  "O perito pode receber honorários proporcionais ao valor obtido pela parte vencedora da causa.",
  [("É vedado ao perito assinar laudo pericial sem ter realizado pessoalmente o exame.",
    "Correta: art. 92."),
   ("É vedado ao médico ser perito do próprio paciente ou de pessoa de sua família.",
    "Correta: art. 93."),
   ("É vedado ao perito deixar de atuar com absoluta isenção quando designado.",
    "Correta: art. 98."),
   ("É vedado ao perito, salvo urgência, modificar procedimentos propedêuticos ou terapêuticos instituídos.",
    "Correta: art. 97.")],
  "CEM, art. 96: é vedado receber remuneração ou gratificação por valores vinculados à glosa ou ao sucesso da causa quando na função de perito ou auditor.",
  "Resolução CFM 2.217/2018 (CEM), arts. 92, 93, 96, 97 e 98", "Honorário de êxito compromete a isenção do perito.")

q(Q, D, BIO, "CPC – conteúdo do laudo", 2, DIR, I,
  "Conforme o art. 473 do Código de Processo Civil, o laudo pericial deve conter os itens abaixo, EXCETO:",
  "opinião pessoal do perito sobre questões jurídicas que ultrapassem o exame técnico do objeto da perícia.",
  [("exposição do objeto da perícia.", "Correta: art. 473, I."),
   ("análise técnica ou científica realizada pelo perito.", "Correta: art. 473, II."),
   ("indicação do método utilizado, demonstrando ser predominantemente aceito pelos especialistas.", "Correta: art. 473, III."),
   ("resposta conclusiva a todos os quesitos apresentados pelo juiz, pelas partes e pelo Ministério Público.", "Correta: art. 473, IV.")],
  "CPC, art. 473: exposição do objeto, análise técnica, método e respostas conclusivas aos quesitos. O § 2º veda ao perito ultrapassar os limites de sua designação e emitir opiniões pessoais que excedam o exame técnico.",
  "CPC (Lei 13.105/2015), art. 473", "O perito responde ao técnico; quem decide o jurídico é o juiz.")

# ---------------------------------------------------------------- Capacidade laborativa
q(Q, D, CAP, "Diagnóstico × incapacidade × trabalho habitual", 2, SIT, C,
  "Caixa de supermercado de 61 anos, com cardiopatia chagásica e marca-passo, comparece à perícia no 22º dia "
  "de atestado de 30 dias, referindo dispneia ao banho. Ao exame, está compensado em repouso. Sobre a conduta "
  "pericial, assinale a afirmativa CORRETA.",
  "A conclusão depende da correlação entre achados, gravidade funcional e exigências da função habitual.",
  [("A conclusão deve seguir o atestado do médico assistente, que vincula o perito quanto ao prazo.",
    "O atestado é elemento de prova, mas não vincula o perito."),
   ("A conclusão deve ser pela incapacidade permanente, pois cardiopatia chagásica com marca-passo é sempre incapacitante.",
    "Diagnóstico não equivale a incapacidade; o grau funcional é que decide."),
   ("A conclusão deve ser pela capacidade, pois o exame em repouso normal afasta a dispneia relatada.",
    "Dispneia aos esforços (classe funcional) não se exclui com exame em repouso."),
   ("A conclusão deve incluir prescrição de novo fármaco, conduta que cabe ao perito ao identificar tratamento insuficiente.",
    "O perito não modifica o tratamento do assistente (CEM, art. 97).")],
  "Incapacidade é conclusão funcional: correlaciona história, exame, classe funcional (NYHA) e exigências da atividade habitual. O atestado do assistente não vincula. O perito não prescreve nem altera tratamento. Caso inspirado no Cebraspe MPS 2025 (itens 52–53).",
  "Manual Técnico de Perícia Médica Previdenciária (INSS); CEM, art. 97",
  "Concluir só pelo diagnóstico ou só pelo exame em repouso.")
