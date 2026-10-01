from _base import q

Q = []
D = "Informática"
SIT, DIR = "situacional", "direto"
C, I = "CORRETA", "INCORRETA"

q(Q, D, "Utilização de planilhas eletrônicas", "Referência absoluta", 2, SIT, C,
  "No Excel, a célula B1 contém o valor da diária (R$ 150). Em A2:A10 há a quantidade de dias de cada "
  "servidor, e a fórmula de B2 será copiada até B10 para calcular o total de cada um. Assinale a "
  "afirmativa CORRETA.",
  "A fórmula adequada em B2 é =A2*$B$1, pois a referência absoluta mantém fixa a célula da diária ao copiar.",
  [("A fórmula adequada em B2 é =A2*B1, pois o Excel ajusta B1 automaticamente para o valor correto em cada linha.",
    "Copiada, B1 viraria B2, B3… e o cálculo ficaria errado."),
   ("A fórmula adequada em B2 é =$A$2*B1, pois a referência absoluta deve recair sobre a quantidade de dias.",
    "A célula que deve ficar fixa é a da diária, não a quantidade."),
   ("A fórmula adequada em B2 é =A2*#B#1, pois o símbolo # fixa linha e coluna da célula referenciada.",
    "O símbolo de referência absoluta no Excel é $."),
   ("A fórmula adequada em B2 é =SOMA(A2:B1), pois a função soma multiplica a quantidade pelo valor da diária.",
    "SOMA adiciona valores; não multiplica.")],
  "O $ antes da coluna e da linha ($B$1) torna a referência absoluta: ao copiar a fórmula, A2 se ajusta (A3, A4…) e $B$1 permanece fixo.",
  "Microsoft Excel – referências relativas e absolutas", "Fixar a célula errada ou usar símbolo errado.")

q(Q, D, "Utilização de planilhas eletrônicas", "Função SE", 2, SIT, C,
  "Em uma planilha do Excel em português, a coluna C traz a nota da prova objetiva de cada candidato. "
  "Deseja-se exibir em D2 'Aprovado' se a nota em C2 for maior ou igual a 70 e 'Eliminado' caso "
  "contrário. Assinale a afirmativa CORRETA.",
  "A fórmula adequada é =SE(C2>=70;\"Aprovado\";\"Eliminado\"), com ponto e vírgula separando os argumentos.",
  [("A fórmula adequada é =SE(C2>70;\"Aprovado\";\"Eliminado\"), pois o operador > inclui a nota 70.",
    "O operador > exclui o 70; o correto é >=."),
   ("A fórmula adequada é =SE(C2>=70;Aprovado;Eliminado), pois textos dispensam aspas em funções lógicas.",
    "Textos devem estar entre aspas."),
   ("A fórmula adequada é =CONT.SE(C2>=70;\"Aprovado\";\"Eliminado\"), pois a função conta os aprovados.",
    "CONT.SE conta células que atendem a critério; não retorna textos condicionais."),
   ("A fórmula adequada é =SE(\"Aprovado\";C2>=70;\"Eliminado\"), pois o primeiro argumento é o valor verdadeiro.",
    "O primeiro argumento é o teste lógico.")],
  "Sintaxe em PT-BR: =SE(teste_lógico;valor_se_verdadeiro;valor_se_falso). Textos entre aspas; >= inclui o valor limite.",
  "Microsoft Excel – função SE", "Operador > × >= e ordem dos argumentos.")

q(Q, D, "Utilização de planilhas eletrônicas", "CONT.SE e MÉDIA", 2, DIR, C,
  "Em planilha do Excel, o intervalo A1:A20 contém os valores 'Apto' ou 'Inapto' de laudos periciais. "
  "Assinale a afirmativa CORRETA sobre a função que conta quantos laudos são 'Apto'.",
  "A fórmula =CONT.SE(A1:A20;\"Apto\") retorna o número de células do intervalo cujo conteúdo é 'Apto'.",
  [("A fórmula =SOMA(A1:A20;\"Apto\") retorna o número de células do intervalo cujo conteúdo é 'Apto'.",
    "SOMA adiciona números; não conta textos por critério."),
   ("A fórmula =CONT.NÚM(A1:A20;\"Apto\") retorna o número de células do intervalo cujo conteúdo é 'Apto'.",
    "CONT.NÚM conta células com números e não aceita critério."),
   ("A fórmula =MÉDIA(A1:A20;\"Apto\") retorna o número de células do intervalo cujo conteúdo é 'Apto'.",
    "MÉDIA calcula média aritmética de números."),
   ("A fórmula =CONT.VALORES(\"Apto\";A1:A20) retorna o número de células do intervalo cujo conteúdo é 'Apto'.",
    "CONT.VALORES conta células não vazias, sem critério.")],
  "CONT.SE(intervalo;critério) conta as células que atendem ao critério. CONT.VALORES conta não vazias; CONT.NÚM conta números.",
  "Microsoft Excel – funções de contagem", "Funções de contagem parecidas.")

q(Q, D, "Aplicativos de escritório", "Atalhos do Word em PT-BR", 2, DIR, C,
  "No Microsoft Word em português do Brasil, com configuração padrão, assinale a afirmativa CORRETA "
  "sobre teclas de atalho.",
  "O atalho Ctrl+N aplica negrito ao texto selecionado, e Ctrl+B salva o documento.",
  [("O atalho Ctrl+B aplica negrito ao texto selecionado, e Ctrl+N salva o documento.",
    "Inversão: na versão PT-BR, Ctrl+N é negrito e Ctrl+B é salvar."),
   ("O atalho Ctrl+S aplica negrito ao texto selecionado, e Ctrl+B salva o documento.",
    "Ctrl+S é sublinhado no Word PT-BR."),
   ("O atalho Ctrl+N cria um novo documento em branco, e Ctrl+B salva o documento.",
    "Ctrl+N é negrito; novo documento é Ctrl+O."),
   ("O atalho Ctrl+I aplica negrito ao texto selecionado, e Ctrl+S salva o documento.",
    "Ctrl+I é itálico; Ctrl+S é sublinhado.")],
  "Word PT-BR: Ctrl+N negrito; Ctrl+I itálico; Ctrl+S sublinhado; Ctrl+B salvar; Ctrl+O novo; Ctrl+A abrir; Ctrl+P imprimir; Ctrl+T selecionar tudo; Ctrl+E centralizar; Ctrl+J justificar.",
  "Microsoft Word – atalhos (versão em português)", "Confusão com os atalhos da versão em inglês (Ctrl+B = bold).", verificar=True)

q(Q, D, "Conceitos de sistemas operacionais", "Atalhos do Windows", 1, DIR, C,
  "No Windows 10/11, com configuração padrão, assinale a afirmativa CORRETA sobre teclas de atalho.",
  "A combinação Windows+L bloqueia a sessão, exigindo nova autenticação para retomar o uso.",
  [("A combinação Windows+L abre o Explorador de Arquivos, exibindo as unidades e pastas do computador.",
    "O Explorador é Windows+E."),
   ("A combinação Windows+L minimiza todas as janelas e exibe a área de trabalho do usuário.",
    "Exibir a área de trabalho é Windows+D."),
   ("A combinação Windows+L abre o Gerenciador de Tarefas, permitindo encerrar programas travados.",
    "Gerenciador de Tarefas é Ctrl+Shift+Esc."),
   ("A combinação Windows+L abre as Configurações do sistema, permitindo alterar preferências.",
    "Configurações é Windows+I.")],
  "Windows+L bloqueia; Windows+E abre o Explorador; Windows+D mostra a área de trabalho; Windows+I abre Configurações; Ctrl+Shift+Esc abre o Gerenciador de Tarefas.",
  "Microsoft Windows – atalhos de teclado", "Atalhos com a tecla Windows confundíveis.")

q(Q, D, "Conceitos sobre armazenamento e gerenciamento de arquivos", "Exclusão permanente", 2, SIT, C,
  "Servidora selecionou no Explorador de Arquivos do Windows um arquivo com dados de periciandos, em "
  "disco local, e pressionou Shift+Delete, confirmando a ação. Assinale a afirmativa CORRETA.",
  "O arquivo é excluído sem passar pela Lixeira, não podendo ser restaurado por ela.",
  [("O arquivo é enviado à Lixeira, podendo ser restaurado à pasta original a qualquer momento.",
    "Shift+Delete ignora a Lixeira."),
   ("O arquivo é copiado para a área de transferência, sendo excluído apenas após ser colado em outro local.",
    "Isso descreve recortar (Ctrl+X)."),
   ("O arquivo é renomeado, recebendo a extensão .bak para indicar que se trata de cópia de segurança.",
    "Renomear é F2."),
   ("O arquivo é ocultado, permanecendo no disco, mas invisível no Explorador até nova configuração.",
    "Ocultar é atributo de propriedades.")],
  "Delete envia à Lixeira (em discos locais); Shift+Delete exclui permanentemente, sem passar pela Lixeira.",
  "Microsoft Windows – gerenciamento de arquivos", "Confundir com recortar/ocultar.")

q(Q, D, "Conceitos de segurança da informação e proteção de dados", "Malwares", 2, DIR, C,
  "Considerando os tipos de códigos maliciosos, assinale a afirmativa CORRETA.",
  "O ransomware torna os dados inacessíveis, geralmente por criptografia, e exige resgate para liberá-los.",
  [("O ransomware registra as teclas digitadas pelo usuário para capturar senhas e enviá-las a terceiros.",
    "Isso é keylogger (tipo de spyware)."),
   ("O ransomware propaga-se automaticamente pela rede sem precisar de arquivo hospedeiro, explorando vulnerabilidades.",
    "Isso é worm."),
   ("O ransomware disfarça-se de programa legítimo para instalar funções maliciosas sem o conhecimento do usuário.",
    "Isso é cavalo de troia (trojan)."),
   ("O ransomware mantém acesso remoto oculto ao equipamento, permitindo o retorno do invasor posteriormente.",
    "Isso é backdoor.")],
  "Ransomware: sequestra dados (criptografa) e exige resgate. Worm: se propaga sozinho. Trojan: disfarça-se de programa legítimo. Keylogger: captura teclas. Backdoor: acesso remoto oculto.",
  "Cartilha de Segurança para Internet (CERT.br)", "Troca entre malwares.")

q(Q, D, "Conceitos de segurança da informação e proteção de dados", "Phishing", 1, SIT, C,
  "Servidor recebeu e-mail com logotipo do banco solicitando que clicasse em link para 'atualizar dados "
  "cadastrais' em até 24 horas, sob pena de bloqueio da conta. Assinale a afirmativa CORRETA.",
  "Trata-se de tentativa de phishing, golpe que usa mensagens falsas para obter dados pessoais.",
  [("Trata-se de spam legítimo, comunicação comercial autorizada que não oferece risco ao usuário.",
    "A mensagem induz a fornecer dados sob ameaça: phishing."),
   ("Trata-se de ataque de negação de serviço, que torna indisponível o servidor de e-mail institucional.",
    "Negação de serviço (DoS) sobrecarrega serviços; não é o caso."),
   ("Trata-se de tentativa de phishing, golpe que só ocorre por e-mail, sendo impossível por SMS ou aplicativo.",
    "Phishing ocorre por vários canais (smishing, mensagens etc.)."),
   ("Trata-se de backup automático, procedimento do banco para resguardar os dados do correntista.",
    "Backup não exige que o usuário clique em links.")],
  "Phishing: tentativa de obter dados pessoais/financeiros por mensagens que se passam por instituições conhecidas, frequentemente com senso de urgência.",
  "Cartilha de Segurança para Internet (CERT.br)", "Absoluto ('só ocorre por e-mail').")

q(Q, D, "Ferramentas de backup e recuperação de dados", "Backup incremental × diferencial", 3, DIR, C,
  "Considerando os tipos de backup, assinale a afirmativa CORRETA.",
  "O backup incremental copia só o que mudou desde o último backup de qualquer tipo, exigindo o completo e todos os incrementais.",
  [("O backup incremental copia todos os arquivos alterados desde o último backup completo, exigindo, na restauração, apenas o último incremental.",
    "Isso descreve o diferencial (e o diferencial exige o completo + o último diferencial)."),
   ("O backup diferencial copia apenas os arquivos alterados desde o último backup de qualquer tipo, sendo o mais rápido de restaurar.",
    "Diferencial copia o alterado desde o último COMPLETO."),
   ("O backup incremental copia todos os arquivos do sistema a cada execução, independentemente de alteração.",
    "Isso é o backup completo (full)."),
   ("O backup completo copia apenas os arquivos alterados, sendo dispensável para restaurar os backups incrementais.",
    "O completo copia tudo e é a base da restauração.")],
  "Completo: copia tudo. Incremental: alterados desde o último backup (completo ou incremental) — backup rápido, restauração mais trabalhosa. Diferencial: alterados desde o último completo — restauração exige o completo + o último diferencial.",
  "Segurança da informação – políticas de backup", "Troca incremental × diferencial.")

q(Q, D, "Conceitos sobre protocolos de comunicação na internet", "Protocolos de e-mail", 2, DIR, C,
  "Considerando os protocolos utilizados no serviço de correio eletrônico, assinale a afirmativa CORRETA.",
  "O SMTP é usado no envio de mensagens, enquanto o IMAP permite acessar e sincronizar as mensagens mantidas no servidor.",
  [("O IMAP é usado no envio de mensagens, enquanto o SMTP permite acessar e sincronizar as mensagens no servidor.",
    "Inversão: SMTP envia; IMAP acessa/sincroniza."),
   ("O HTTP é usado no envio de mensagens, enquanto o FTP permite acessar e sincronizar as mensagens mantidas no servidor.",
    "HTTP é para páginas web; FTP para transferência de arquivos."),
   ("O POP3 é usado no envio de mensagens, enquanto o DNS permite acessar e sincronizar as mensagens mantidas no servidor.",
    "POP3 recebe; DNS resolve nomes."),
   ("O SMTP é usado no recebimento de mensagens, enquanto o POP3 sincroniza pastas entre vários dispositivos.",
    "SMTP envia; POP3 tende a baixar mensagens, sem sincronizar pastas.")],
  "SMTP: envio. POP3: recebimento, geralmente baixando as mensagens para o dispositivo. IMAP: acesso às mensagens no servidor, sincronizando entre dispositivos.",
  "Redes de computadores – protocolos de aplicação", "Inversão de funções entre protocolos.")

q(Q, D, "E-mail e comunicação eletrônica no ambiente corporativo", "Cópia oculta (CCO)", 1, SIT, C,
  "A coordenação da perícia vai enviar convocação por e-mail a 40 periciandos e não deseja que um "
  "destinatário veja o endereço dos demais. Assinale a afirmativa CORRETA.",
  "Os endereços devem ser incluídos no campo CCO (cópia oculta), que impede a visualização dos demais destinatários.",
  [("Os endereços devem ser incluídos no campo CC (com cópia), que impede a visualização dos demais destinatários.",
    "No campo CC os endereços ficam visíveis a todos."),
   ("Os endereços devem ser incluídos no campo Para, que oculta automaticamente os destinatários após o envio.",
    "O campo Para exibe os destinatários."),
   ("Os endereços devem ser incluídos no campo Assunto, separados por ponto e vírgula, para manter o sigilo.",
    "O campo Assunto não é campo de destinatário."),
   ("Os endereços devem ser incluídos no campo CCO, que, porém, os revela a quem responde a todos.",
    "Destinatários em CCO não são revelados a quem responde a todos.")],
  "CCO (Cco/Bcc): os destinatários não aparecem para os demais. CC: cópia visível.",
  "Correio eletrônico – campos de endereçamento", "Troca CC × CCO.")

q(Q, D, "Noções de computação em nuvem", "Modelos de serviço", 2, DIR, C,
  "Considerando os modelos de serviço de computação em nuvem, assinale a afirmativa CORRETA.",
  "No modelo SaaS, o usuário utiliza o software pronto pela internet, sem gerenciar a infraestrutura subjacente.",
  [("No modelo SaaS, o usuário contrata servidores virtuais e gerencia o sistema operacional e as aplicações instaladas.",
    "Isso descreve IaaS."),
   ("No modelo IaaS, o usuário utiliza o software pronto pela internet, sem gerenciar a infraestrutura em que ele roda.",
    "Isso descreve SaaS."),
   ("No modelo PaaS, o usuário recebe apenas o hardware físico, devendo instalá-lo em suas próprias dependências.",
    "PaaS oferece plataforma para desenvolver e implantar aplicações."),
   ("No modelo SaaS, o usuário é responsável pela manutenção física dos servidores do provedor de nuvem.",
    "A infraestrutura é responsabilidade do provedor.")],
  "IaaS: infraestrutura (máquinas virtuais, armazenamento). PaaS: plataforma de desenvolvimento/execução. SaaS: software pronto acessado pela internet (ex.: webmail, suítes online).",
  "Computação em nuvem – NIST SP 800-145", "Troca entre IaaS, PaaS e SaaS.")

q(Q, D, "Conceitos de segurança da informação e proteção de dados", "LGPD – dado sensível", 2, SIT, C,
  "O setor de perícia mantém planilhas com nome, CPF e diagnósticos (CID) dos servidores avaliados. "
  "Considerando a Lei Geral de Proteção de Dados (Lei nº 13.709/2018), assinale a afirmativa CORRETA.",
  "Dados referentes à saúde são dados pessoais sensíveis, cujo tratamento exige hipóteses legais específicas.",
  [("Dados referentes à saúde são dados pessoais comuns, equiparados ao nome e ao endereço para fins de proteção legal.",
    "A LGPD classifica dado de saúde como sensível (art. 5º, II)."),
   ("Dados referentes à saúde ficam fora do alcance da LGPD quando tratados pelo poder público em suas atividades.",
    "O poder público também se submete à LGPD, com regras próprias."),
   ("Dados referentes à saúde podem ser compartilhados livremente entre setores, desde que anonimizados apenas pelo CPF.",
    "Retirar só o CPF não anonimiza; o compartilhamento exige base legal."),
   ("Dados referentes à saúde são dados pessoais sensíveis, cujo tratamento depende sempre do consentimento do titular.",
    "O art. 11 prevê hipóteses sem consentimento (ex.: cumprimento de obrigação legal, tutela da saúde).")],
  "Art. 5º, II, da LGPD: dado pessoal sensível inclui dado referente à saúde. Art. 11: hipóteses de tratamento de dados sensíveis, com e sem consentimento.",
  "Lei 13.709/2018 (LGPD), arts. 5º, II, e 11", "'Sempre do consentimento' e exclusão indevida do poder público.")
