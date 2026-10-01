from _base import q

Q = []
D = "Português"
SIT, DIR = "situacional", "direto"
C, I = "CORRETA", "INCORRETA"

TEXTOS = {
"T1": """O laudo que ninguém lê

Há documentos que nascem para ser arquivados. O laudo pericial, embora pareça pertencer a essa
família, carrega uma ambição maior: traduzir um corpo em palavras capazes de orientar decisões que
mudam vidas. Quando um perito conclui que alguém está incapaz para o trabalho, não descreve apenas
uma condição clínica; autoriza, em certa medida, um novo arranjo de existência.

Por isso mesmo, causa estranheza que tantos laudos sejam escritos como se ninguém fosse lê-los.
Frases truncadas, abreviaturas obscuras e conclusões sem fundamentação transformam o documento em
enigma. O periciando não o compreende, o juiz hesita, o advogado o contesta. E o perito, que deveria
ser a voz técnica do processo, torna-se apenas mais um ruído.

Escrever com clareza, contudo, não significa simplificar o que é complexo. Significa organizar o
raciocínio de modo que o leitor percorra o mesmo caminho percorrido pelo autor: da história ao exame,
do exame à análise, da análise à conclusão. Um laudo claro não é aquele que dispensa termos técnicos,
mas aquele que os explica quando necessário e os articula em uma argumentação verificável.

Talvez o maior desafio esteja em reconhecer que a escrita também é parte do ato pericial. Não há
exame bem feito que sobreviva a um texto mal construído.""",

"T2": """Território vivo

Durante muito tempo, o território foi tratado pela saúde pública como simples recorte geográfico:
linhas traçadas no mapa para distribuir responsabilidades entre as equipes. Essa visão, embora útil
para fins administrativos, revelou-se insuficiente para compreender por que pessoas que vivem a
poucos quarteirões de distância adoecem e morrem de maneiras tão diferentes.

O conceito de território vivo propõe outra leitura. Nele, o espaço não é cenário neutro, mas produto
das relações sociais, econômicas e culturais que ali se estabelecem. A ausência de saneamento, a
violência, a distância até a escola e a oferta de trabalho compõem uma paisagem que a equipe de saúde
precisa conhecer se quiser intervir de forma efetiva.

Conhecer o território, entretanto, não se resume a cadastrar famílias. Exige escuta, presença e
disposição para reconhecer saberes que não cabem nos formulários. O agente comunitário que conhece a
história de cada rua frequentemente percebe antes do sistema de informação aquilo que os indicadores
só mostrarão meses depois.

Assim, mapear deixa de ser tarefa burocrática e passa a ser exercício de cuidado.""",
}

# ---------------------------------------------------------------- Texto 1
q(Q, D, "Interpretação e Análise Textual", "Ideia principal", 2, DIR, C,
  "Leia o texto 'O laudo que ninguém lê' para responder. Considerando a ideia central defendida pelo "
  "autor, assinale a afirmativa CORRETA.",
  "O texto sustenta que a clareza da escrita integra o ato pericial, pois o laudo orienta decisões sobre terceiros.",
  [("O texto sustenta que a clareza da escrita exige a eliminação de termos técnicos, pois o laudo se destina a leitores leigos.",
    "O 3º parágrafo diz que um laudo claro NÃO dispensa termos técnicos."),
   ("O texto sustenta que o laudo pericial é documento essencialmente burocrático, destinado sobretudo ao arquivamento.",
    "O texto afirma que o laudo 'carrega uma ambição maior' que o arquivamento."),
   ("O texto sustenta que a qualidade do exame clínico compensa eventuais falhas na redação do laudo pericial.",
    "A última frase afirma o contrário."),
   ("O texto sustenta que a responsabilidade pela compreensão do laudo cabe principalmente ao juiz e ao advogado.",
    "O texto atribui ao perito a responsabilidade pela clareza.")],
  "A tese aparece no último parágrafo ('a escrita também é parte do ato pericial') e é preparada pela ideia de que o laudo orienta decisões que mudam vidas.",
  "Interpretação de texto – ideia principal", "Distrator que absolutiza ('eliminação de termos técnicos').", texto="T1")

q(Q, D, "Interpretação e Análise Textual", "Coesão – conectivo", 2, DIR, C,
  "No trecho 'Escrever com clareza, contudo, não significa simplificar o que é complexo', do texto 'O "
  "laudo que ninguém lê', o conectivo destacado pode ser substituído, sem alteração de sentido, por:",
  "no entanto, pois o conectivo estabelece relação de oposição com o que foi dito.",
  [("portanto, pois o conectivo estabelece relação de conclusão com a ideia anterior.",
    "'Contudo' é adversativo, não conclusivo."),
   ("porque, pois o conectivo estabelece relação de causa com a ideia anterior.",
    "'Contudo' não expressa causa."),
   ("além disso, pois o conectivo estabelece relação de adição com a ideia anterior.",
    "'Contudo' não expressa adição."),
   ("assim, pois o conectivo estabelece relação de consequência com a ideia anterior.",
    "'Contudo' não expressa consequência.")],
  "'Contudo' é conjunção coordenativa adversativa, equivalente a 'no entanto', 'todavia', 'entretanto', 'porém'.",
  "Coesão textual – conectivos", "Troca de relação lógica entre conectivos.", texto="T1")

q(Q, D, "Interpretação e Análise Textual", "Inferência", 3, DIR, C,
  "No 2º parágrafo do texto 'O laudo que ninguém lê', afirma-se que o perito 'torna-se apenas mais um "
  "ruído'. Pode-se inferir dessa expressão que:",
  "o laudo obscuro faz o perito perder a função de esclarecer, passando a gerar mais dúvidas no processo.",
  [("o laudo obscuro faz o perito ganhar relevância, pois suas conclusões passam a ser mais debatidas no processo.",
    "'Ruído' tem sentido negativo: interferência que atrapalha a comunicação."),
   ("o laudo obscuro faz o perito ser substituído por outro profissional, por determinação expressa do juiz.",
    "O texto não menciona substituição."),
   ("o laudo obscuro faz o perito ser responsabilizado criminalmente, por induzir o juiz a erro na sentença.",
    "Não há referência a responsabilização criminal."),
   ("o laudo obscuro faz o perito ser ignorado pelo advogado, que deixa de contestar as conclusões apresentadas.",
    "O texto diz que o advogado o contesta.")],
  "A metáfora opõe 'voz técnica' a 'ruído': em vez de esclarecer, o laudo obscuro acrescenta confusão.",
  "Interpretação – inferência e linguagem figurada", "Distratores que extrapolam o texto.", texto="T1")

q(Q, D, "Sintaxe", "Concordância verbal", 2, DIR, C,
  "No trecho 'Há documentos que nascem para ser arquivados', do texto 'O laudo que ninguém lê', o verbo "
  "'haver' está corretamente empregado. Assinale a alternativa em que o verbo 'haver' também está "
  "empregado de acordo com a norma-padrão.",
  "Houve muitas contestações ao laudo apresentado na audiência.",
  [("Haviam muitas contestações ao laudo apresentado na audiência.",
    "'Haver' no sentido de existir é impessoal: fica no singular."),
   ("Houveram muitas contestações ao laudo apresentado na audiência.",
    "'Haver' no sentido de existir/ocorrer é impessoal: 'houve'."),
   ("Devem haver muitas contestações ao laudo apresentado na audiência.",
    "O auxiliar também fica no singular: 'deve haver'."),
   ("Hão muitas contestações ao laudo apresentado na audiência.",
    "Impessoal: 'há'.")],
  "'Haver' com sentido de existir ou ocorrer é impessoal e fica na 3ª pessoa do singular, contaminando o auxiliar da locução ('deve haver').",
  "Gramática normativa – concordância verbal (verbos impessoais)", "Concordar 'haver' com o substantivo plural.", texto="T1")

# ---------------------------------------------------------------- Texto 2
q(Q, D, "Interpretação e Análise Textual", "Ideia principal", 2, DIR, C,
  "Leia o texto 'Território vivo' para responder. De acordo com o texto, assinale a afirmativa CORRETA.",
  "O território deve ser compreendido como produto de relações sociais, econômicas e culturais, não só como recorte.",
  [("O território deve ser compreendido apenas como recorte geográfico, útil para distribuir responsabilidades entre equipes.",
    "O texto critica essa visão por ser insuficiente."),
   ("O território deve ser compreendido a partir do cadastro das famílias, que esgota o conhecimento necessário à equipe.",
    "O 3º parágrafo afirma que conhecer o território não se resume a cadastrar famílias."),
   ("O território deve ser compreendido pelos sistemas de informação, que antecipam o que os agentes comunitários percebem.",
    "O texto afirma o oposto: o agente percebe antes do sistema."),
   ("O território deve ser compreendido como cenário neutro, no qual as equipes aplicam protocolos padronizados.",
    "O texto nega que o espaço seja cenário neutro.")],
  "O 2º parágrafo define território vivo como produto das relações sociais, econômicas e culturais.",
  "Interpretação de texto – ideia principal", "Inversão do ponto de vista do autor.", texto="T2")

q(Q, D, "Semântica", "Sentido contextual", 2, DIR, C,
  "No trecho 'compõem uma paisagem que a equipe de saúde precisa conhecer', do texto 'Território vivo', "
  "a palavra 'paisagem' é empregada em sentido:",
  "conotativo, referindo-se ao conjunto de condições sociais que caracterizam o território.",
  [("denotativo, referindo-se à vista natural observada pela equipe durante as visitas domiciliares.",
    "No contexto, 'paisagem' não designa vista natural."),
   ("denotativo, referindo-se ao mapa físico elaborado pela equipe para delimitar as microáreas.",
    "O texto não se refere ao mapa físico."),
   ("conotativo, referindo-se à beleza dos bairros visitados pelos agentes comunitários de saúde.",
    "O sentido não é estético."),
   ("técnico, referindo-se ao conceito de paisagem urbana adotado pelo planejamento municipal.",
    "Não há uso técnico do termo.")],
  "'Paisagem' é usada em sentido figurado (conotativo) para designar o conjunto formado por saneamento, violência, distância da escola e oferta de trabalho.",
  "Semântica – denotação e conotação", "Tomar o sentido figurado como literal.", texto="T2")

q(Q, D, "Interpretação e Análise Textual", "Coesão – referência", 2, DIR, C,
  "No trecho 'Nele, o espaço não é cenário neutro', do 2º parágrafo do texto 'Território vivo', o termo "
  "'Nele' retoma:",
  "o conceito de território vivo, apresentado no período imediatamente anterior.",
  [("o recorte geográfico, apresentado no primeiro parágrafo como visão tradicional.",
    "O antecedente imediato é 'O conceito de território vivo'."),
   ("o mapa das equipes, mencionado como instrumento de distribuição de responsabilidades.",
    "Não há referência a esse termo."),
   ("o sistema de informação, apresentado como fonte dos indicadores de saúde.",
    "O sistema de informação só aparece no 3º parágrafo."),
   ("o quarteirão onde vivem as pessoas, mencionado ao final do primeiro parágrafo.",
    "Não retoma 'quarteirões'.")],
  "'Nele' (em + ele) é elemento coesivo anafórico que retoma 'o conceito de território vivo'.",
  "Coesão textual – referenciação", "Antecedentes plausíveis, mas distantes.", texto="T2")

q(Q, D, "Sintaxe", "Pontuação", 3, DIR, C,
  "Considere o trecho do texto 'Território vivo': 'Conhecer o território, entretanto, não se resume a "
  "cadastrar famílias.' Assinale a afirmativa CORRETA sobre a pontuação.",
  "As vírgulas isolam a conjunção deslocada 'entretanto', sendo, por isso, obrigatórias.",
  [("As vírgulas separam o sujeito do verbo, uso permitido sempre que o sujeito for oracional.",
    "É vedado separar sujeito e verbo por uma única vírgula; aqui as vírgulas isolam a conjunção intercalada."),
   ("As vírgulas são facultativas, podendo ser retiradas sem prejuízo à norma-padrão.",
    "Conjunção intercalada deve vir entre vírgulas."),
   ("As vírgulas isolam um aposto explicativo que define o termo 'território'.",
    "'Entretanto' é conjunção, não aposto."),
   ("As vírgulas isolam um vocativo dirigido ao leitor do texto.",
    "Não há vocativo.")],
  "Conjunção coordenativa deslocada para o meio da oração ('entretanto', 'porém', 'contudo') deve ser isolada por vírgulas.",
  "Gramática normativa – pontuação", "Confundir conjunção intercalada com aposto ou separação sujeito/verbo.", texto="T2")

# ---------------------------------------------------------------- Questões avulsas
q(Q, D, "Sintaxe", "Crase", 2, DIR, C,
  "Assinale a alternativa em que o uso do acento indicativo de crase está de acordo com a norma-padrão.",
  "O perito referiu-se à conclusão do laudo durante a audiência.",
  [("O perito referiu-se à um laudo anterior durante a audiência.",
    "Não há crase antes de artigo indefinido 'um'."),
   ("O perito começou à examinar o periciando na audiência.",
    "Não há crase antes de verbo."),
   ("O perito dirigiu-se à Vossa Excelência durante a audiência.",
    "Não há crase antes de pronome de tratamento (exceto senhora/senhorita/dona)."),
   ("O perito chegou à pé ao local da audiência.",
    "Não há crase antes de palavra masculina.")],
  "'Referir-se a' + 'a conclusão' (artigo feminino) = 'à conclusão'. Não há crase antes de verbo, de palavra masculina, de artigo indefinido e da maioria dos pronomes de tratamento.",
  "Gramática normativa – crase", "Casos clássicos de proibição de crase.")

q(Q, D, "Sintaxe", "Regência verbal", 3, DIR, C,
  "Assinale a alternativa em que a regência verbal está de acordo com a norma-padrão.",
  "A perita assistiu ao vídeo da audiência antes de concluir o laudo.",
  [("A perita assistiu o vídeo da audiência antes de concluir o laudo.",
    "No sentido de ver, 'assistir' é transitivo indireto: 'assistiu ao'."),
   ("A perita preferia mais revisar o laudo do que entregá-lo às pressas.",
    "'Preferir' rege 'a', sem 'mais' e sem 'do que': preferia revisar a entregar."),
   ("A perita obedeceu o protocolo estabelecido pelo instituto.",
    "'Obedecer' é transitivo indireto: obedeceu ao protocolo."),
   ("A perita visava o cargo de coordenação desde o concurso.",
    "'Visar' no sentido de almejar rege 'a': visava ao cargo.")],
  "Assistir (ver) → assistir a; preferir algo a algo; obedecer a; visar (almejar) → visar a.",
  "Gramática normativa – regência verbal", "Regências que divergem do uso coloquial.")

q(Q, D, "Fonologia", "Acentuação (Acordo Ortográfico)", 2, DIR, C,
  "Considerando as regras de acentuação gráfica vigentes após o Acordo Ortográfico, assinale a "
  "alternativa em que todas as palavras estão corretamente grafadas.",
  "ideia, heroico, voo, creem",
  [("idéia, heróico, vôo, crêem",
    "Grafias anteriores ao Acordo; perderam o acento."),
   ("ideia, heróico, voo, creem",
    "Paroxítona com ditongo aberto 'oi' perdeu o acento: heroico."),
   ("idéia, heroico, vôo, creem",
    "'Ideia' e 'voo' perderam o acento."),
   ("ideia, heroico, vôo, crêem",
    "'Voo' e 'creem' perderam o acento.")],
  "Pelo Acordo, perderam o acento os ditongos abertos 'ei' e 'oi' em paroxítonas (ideia, heroico) e os hiatos 'oo' e 'ee' (voo, creem).",
  "Acordo Ortográfico de 1990 (vigente desde 2016)", "Grafias antigas misturadas às novas.")

q(Q, D, "Redação Oficial", "Pronomes de tratamento e fecho", 2, SIT, C,
  "A perita municipal precisa encaminhar ofício ao Juiz de Direito da comarca. Considerando o Manual de "
  "Redação da Presidência da República (3ª ed.), assinale a afirmativa CORRETA.",
  "Deve usar o tratamento Vossa Excelência, com concordância na terceira pessoa, e o fecho 'Respeitosamente'.",
  [("Deve usar o tratamento Vossa Senhoria, com concordância na segunda pessoa, e o fecho 'Atenciosamente'.",
    "Juízes recebem Vossa Excelência; a concordância é em 3ª pessoa."),
   ("Deve usar o tratamento Vossa Excelência, com concordância na segunda pessoa do plural, e o fecho 'Cordialmente'.",
    "A concordância é em 3ª pessoa; 'Cordialmente' não é fecho previsto."),
   ("Deve usar o tratamento Vossa Magnificência, com concordância na terceira pessoa, e o fecho 'Respeitosamente'.",
    "Vossa Magnificência é para reitores."),
   ("Deve usar o vocativo 'Digníssimo Senhor Juiz' e o fecho 'Atenciosamente', por ser autoridade de mesma hierarquia.",
    "'Digníssimo' foi abolido; o juiz é autoridade superior para fins de fecho.")],
  "O Manual prevê Vossa Excelência para juízes, com concordância em 3ª pessoa ('Vossa Excelência está'), e o fecho 'Respeitosamente' para autoridades de hierarquia superior; 'Atenciosamente' para mesma hierarquia ou inferior.",
  "Manual de Redação da Presidência da República, 3ª ed. (2018)", "Troca de tratamento e de fecho.", verificar=True)

q(Q, D, "Morfologia", "Formação de palavras", 3, DIR, C,
  "Assinale a alternativa em que a palavra foi formada por derivação parassintética.",
  "entardecer",
  [("infelizmente",
    "Derivação prefixal e sufixal (existe 'infeliz' e existe 'felizmente')."),
   ("girassol",
    "Composição por justaposição."),
   ("combate",
    "Derivação regressiva (de 'combater')."),
   ("planalto",
    "Composição por aglutinação.")],
  "Na parassíntese, prefixo e sufixo entram simultaneamente: não existem 'entarde' nem 'tardecer'. Em 'infelizmente', existem as formas intermediárias.",
  "Gramática normativa – formação de palavras", "Confundir parassíntese com prefixação + sufixação.")
