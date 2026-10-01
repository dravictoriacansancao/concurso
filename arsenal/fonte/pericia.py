from _base import q

Q = []
D = "Perícia"
SIT, DIR = "situacional", "direto"
C, I = "CORRETA", "INCORRETA"

# ---------------------------------------------------------------- Previdenciária
q(Q, D, "Perícia médica previdenciária", "DID, DII e carência", 3, SIT, C,
  "Segurado com primeira filiação ao RGPS em março de 2025 requer auxílio por incapacidade temporária em "
  "agosto de 2025. Documentos mostram lombalgia desde 2023 (DID); em julho de 2025 surgiu hérnia discal "
  "extrusa com déficit motor, fixada como DII. Não há acidente nem doença isenta de carência. "
  "Considerando a Lei nº 8.213/1991, assinale a afirmativa CORRETA.",
  "O ponto decisivo é a carência: sem doze contribuições e fora das hipóteses de isenção, o agravamento não basta para o benefício.",
  [("O ponto decisivo é a preexistência: a doença anterior à filiação impede sempre o benefício, mesmo que a incapacidade decorra de agravamento.",
    "O art. 59, § 1º, ressalva a incapacidade que sobrevém por progressão ou agravamento."),
   ("O ponto decisivo é o agravamento: comprovada a progressão da doença, fica dispensada a carência de doze contribuições mensais.",
    "Agravamento afasta a vedação da preexistência, mas não dispensa a carência."),
   ("O ponto decisivo é a DID: fixada a doença em 2023, o perito deve indeferir por preexistência, sendo irrelevante a data da incapacidade.",
    "O que define o direito é a DII; a DID isolada não basta."),
   ("O ponto decisivo é a DER: a incapacidade deve ser fixada na data do requerimento, momento em que a carência já teria sido cumprida.",
    "A DII é fixada pela evidência médica, não pela DER; e a carência não estaria cumprida.")],
  "Auxílio por incapacidade temporária exige, em regra, carência de 12 contribuições (art. 25, I). A preexistência só não é óbice quando a incapacidade decorre de progressão ou agravamento (art. 59, § 1º), mas isso não supre a carência. Lombalgia/hérnia não está no rol de isenção.",
  "Lei 8.213/1991, arts. 25, I; 26, II; 59, § 1º; 151", "Misturar preexistência e carência: o agravamento resolve uma, não a outra.")

q(Q, D, "Perícia médica previdenciária", "Isenção de carência", 2, SIT, C,
  "Segurada filiada ao RGPS há quatro meses recebe diagnóstico de carcinoma de mama, iniciado após a "
  "filiação, e fica incapacitada durante a quimioterapia. Considerando a Lei nº 8.213/1991, assinale a "
  "afirmativa CORRETA.",
  "A neoplasia maligna acometida após a filiação dispensa a carência, sendo devido o benefício se presente a incapacidade.",
  [("A neoplasia maligna dispensa a carência apenas quando a incapacidade for permanente, exigindo-se doze contribuições para benefício temporário.",
    "A isenção vale para auxílio por incapacidade temporária e aposentadoria por incapacidade permanente."),
   ("A neoplasia maligna dispensa a carência, sendo devido o benefício independentemente da constatação de incapacidade laboral.",
    "A isenção afasta a carência, não a exigência de incapacidade."),
   ("A neoplasia maligna dispensa a carência mesmo quando já existente antes da filiação ao RGPS, sem qualquer ressalva legal.",
    "A isenção exige que o segurado seja acometido após filiar-se (art. 26, II)."),
   ("A neoplasia maligna não integra o rol de doenças que dispensam carência, exigindo-se doze contribuições na data da incapacidade.",
    "Neoplasia maligna integra o rol do art. 151.")],
  "Art. 26, II: independe de carência o auxílio por incapacidade temporária e a aposentadoria por incapacidade permanente ao segurado que, após filiar-se ao RGPS, for acometido de alguma das doenças do art. 151 (entre elas, neoplasia maligna).",
  "Lei 8.213/1991, arts. 26, II, e 151", "Isenção de carência ≠ dispensa de incapacidade; exige acometimento após a filiação.")

q(Q, D, "Perícia médica previdenciária", "Auxílio-acidente – segurados", 3, SIT, C,
  "Motorista de aplicativo, contribuinte individual, sofreu acidente doméstico com amputação da falange "
  "distal do indicador dominante. Após consolidação, há redução da capacidade para a atividade habitual, "
  "sem incapacidade total. Considerando a Lei nº 8.213/1991, assinale a afirmativa CORRETA.",
  "O segurado não faz jus ao auxílio-acidente, pois o benefício não alcança o contribuinte individual, embora dispense carência.",
  [("O segurado faz jus ao auxílio-acidente, pois o benefício alcança todos os segurados do RGPS que sofram acidente de qualquer natureza.",
    "O art. 18, § 1º, restringe o auxílio-acidente a empregado, doméstico, avulso e segurado especial."),
   ("O segurado não faz jus ao auxílio-acidente, pois o benefício só é devido quando o acidente tem natureza ocupacional.",
    "O auxílio-acidente é devido por acidente de qualquer natureza; o óbice é a categoria de segurado."),
   ("O segurado faz jus ao auxílio-acidente, desde que tenha cumprido carência de doze contribuições mensais antes do acidente.",
    "O auxílio-acidente independe de carência e não alcança o contribuinte individual."),
   ("O segurado não faz jus ao auxílio-acidente, pois a amputação de falange não configura sequela consolidada indenizável.",
    "A sequela descrita reduz a capacidade; o óbice é a categoria de segurado.")],
  "O auxílio-acidente é devido, como indenização, após consolidação das lesões decorrentes de acidente de qualquer natureza que resultem em sequela redutora da capacidade (art. 86), independe de carência (art. 26, I) e só é concedido a empregado, empregado doméstico, trabalhador avulso e segurado especial (art. 18, § 1º).",
  "Lei 8.213/1991, arts. 18, § 1º; 26, I; 86", "Atribuir o óbice ao motivo errado (natureza do acidente ou carência).")

q(Q, D, "Perícia médica previdenciária", "Auxílio-acidente – natureza", 2, DIR, C,
  "Considerando o auxílio-acidente disciplinado no art. 86 da Lei nº 8.213/1991, assinale a afirmativa "
  "CORRETA.",
  "O benefício tem natureza indenizatória, é concedido após a consolidação das lesões e permite ao segurado continuar trabalhando.",
  [("O benefício tem natureza substitutiva da renda, é concedido durante o tratamento e impede o retorno do segurado ao trabalho.",
    "É indenizatório, posterior à consolidação, e compatível com o trabalho."),
   ("O benefício tem natureza indenizatória, mas só é concedido quando a sequela gera incapacidade total para o trabalho.",
    "Exige redução da capacidade, não incapacidade total."),
   ("O benefício tem natureza indenizatória, é concedido após a consolidação e corresponde a 100% do salário de benefício.",
    "Corresponde a 50% do salário de benefício."),
   ("O benefício tem natureza assistencial, é concedido independentemente de filiação e cessa quando o segurado volta a trabalhar.",
    "É previdenciário, exige qualidade de segurado e não cessa pelo retorno ao trabalho.")],
  "Art. 86: auxílio-acidente concedido como indenização quando, após consolidação das lesões decorrentes de acidente de qualquer natureza, resultarem sequelas que impliquem redução da capacidade para o trabalho habitual. § 1º: 50% do salário de benefício.",
  "Lei 8.213/1991, art. 86", "Confundir com benefício por incapacidade (substitutivo de renda).")

q(Q, D, "Avaliação de invalidez e incapacidade permanente", "Acréscimo de 25%", 3, SIT, C,
  "Aposentado por incapacidade permanente após AVC evoluiu com hemiplegia e afasia, necessitando de "
  "ajuda de terceiros para alimentação e higiene. O valor de sua aposentadoria já está no teto do RGPS. "
  "Considerando a Lei nº 8.213/1991, assinale a afirmativa CORRETA.",
  "Necessitando de assistência permanente de outra pessoa, faz jus ao acréscimo de 25%, devido ainda que o valor ultrapasse o teto.",
  [("Necessitando de assistência permanente de outra pessoa, faz jus ao acréscimo de 25%, limitado, porém, ao teto do RGPS.",
    "O art. 45, parágrafo único, 'a', admite superar o teto."),
   ("Necessitando de assistência permanente de outra pessoa, faz jus ao acréscimo de 25%, que se incorpora à pensão por morte.",
    "O acréscimo cessa com a morte e não se incorpora à pensão (art. 45, parágrafo único, 'c')."),
   ("Necessitando de assistência de terceiros, faz jus ao acréscimo de 50%, devido a qualquer aposentado do RGPS em igual situação.",
    "O percentual é 25% e a lei o prevê para a aposentadoria por incapacidade permanente."),
   ("Necessitando de assistência de terceiros, não faz jus a acréscimo, pois a dependência funcional já integra a incapacidade permanente.",
    "O acréscimo existe justamente para a dependência de terceiros.")],
  "Art. 45: o valor da aposentadoria por incapacidade permanente do segurado que necessitar da assistência permanente de outra pessoa será acrescido de 25%. Parágrafo único: devido ainda que o valor atinja o limite máximo legal; recalculado com o benefício; cessa com a morte, não se incorporando à pensão.",
  "Lei 8.213/1991, art. 45; Decreto 3.048/1999, Anexo I", "'Limitado ao teto' e 'incorpora à pensão'.")

q(Q, D, "Perícia médica previdenciária", "Art. 101 – tratamento facultativo", 3, SIT, C,
  "Em revisão de auxílio por incapacidade temporária, segurado com hérnia discal recusa a cirurgia "
  "indicada pelo assistente, mas mantém fisioterapia. O perito cogita cessar o benefício pela recusa. "
  "Considerando a Lei nº 8.213/1991, assinale a afirmativa CORRETA.",
  "A recusa à cirurgia não autoriza a cessação, pois o tratamento cirúrgico e a transfusão de sangue são facultativos ao segurado.",
  [("A recusa à cirurgia autoriza a cessação, pois o segurado é obrigado a submeter-se a todo tratamento prescrito pelo médico assistente.",
    "O art. 101 excetua o tratamento cirúrgico e a transfusão, que são facultativos."),
   ("A recusa à cirurgia autoriza a cessação imediata, salvo se o segurado apresentar segunda opinião médica contrária à indicação.",
    "A cirurgia é facultativa independentemente de segunda opinião."),
   ("A recusa à cirurgia não autoriza a cessação, mas obriga a conversão automática em aposentadoria por incapacidade permanente.",
    "Não há conversão automática; mantém-se a avaliação da incapacidade."),
   ("A recusa à cirurgia não autoriza a cessação, e o segurado fica também dispensado de comparecer aos exames periciais periódicos.",
    "O comparecimento ao exame médico continua obrigatório.")],
  "Art. 101: o segurado em gozo de benefício por incapacidade está obrigado a submeter-se a exame médico, a processo de reabilitação profissional e a tratamento gratuito, exceto o cirúrgico e a transfusão de sangue, que são facultativos.",
  "Lei 8.213/1991, art. 101", "Generalizar a obrigação de tratamento.")

q(Q, D, "Incapacidade temporária / permanente", "DCB e prazo estimado", 2, DIR, C,
  "Considerando as regras da Lei nº 8.213/1991 sobre a duração do auxílio por incapacidade temporária, "
  "assinale a afirmativa CORRETA.",
  "Sempre que possível, o ato de concessão fixa prazo estimado; na ausência, o benefício cessa após 120 dias, salvo pedido de prorrogação.",
  [("Sempre que possível, o ato de concessão fixa prazo estimado; na ausência, o benefício é mantido até nova perícia.",
    "Sem prazo fixado, cessa após 120 dias, ressalvada a prorrogação."),
   ("Em nenhuma hipótese o ato de concessão fixa prazo, cabendo ao segurado solicitar a cessação quando recuperar a capacidade.",
    "A lei manda fixar prazo estimado sempre que possível."),
   ("Sempre que possível, o ato de concessão fixa prazo estimado; na ausência, o benefício cessa após 60 dias, vedada a prorrogação.",
    "O prazo supletivo é de 120 dias e a prorrogação é admitida."),
   ("Sempre que possível, o ato de concessão fixa prazo estimado, que não pode ser prorrogado ainda que persista a incapacidade.",
    "O segurado pode requerer prorrogação.")],
  "Art. 60, § 8º: sempre que possível, o ato de concessão ou reativação judicial ou administrativa deverá fixar o prazo estimado para a duração do benefício. § 9º: na ausência de fixação, o benefício cessará após 120 dias, exceto se o segurado requerer a prorrogação.",
  "Lei 8.213/1991, art. 60, §§ 8º e 9º", "Troca do prazo supletivo e vedação inexistente de prorrogação.")

q(Q, D, "Avaliação da capacidade laborativa", "Incapacidade uniprofissional", 2, SIT, C,
  "Pedreiro de 38 anos com ruptura completa do manguito rotador do ombro dominante, em pós-operatório, "
  "está incapaz para elevar o membro acima da cabeça e carregar peso; o ortopedista prevê recuperação em "
  "seis meses. Considerando a avaliação da capacidade laborativa, assinale a afirmativa CORRETA.",
  "Há incapacidade total e temporária para a atividade habitual, com prognóstico de recuperação em alguns meses.",
  [("Há incapacidade total e permanente para qualquer atividade, pois a lesão no membro dominante inviabiliza o trabalho manual.",
    "O prognóstico é de recuperação em 6 meses: temporária e restrita à atividade habitual."),
   ("Há incapacidade parcial e permanente, devendo ser concedido desde logo o auxílio-acidente pela redução da capacidade.",
    "Auxílio-acidente exige consolidação das lesões; ainda há tratamento em curso."),
   ("Há capacidade preservada, pois o segurado pode exercer outra atividade compatível, ainda que não a habitual.",
    "O auxílio por incapacidade temporária considera a atividade habitual (art. 59)."),
   ("Há incapacidade total e temporária, devendo o segurado ser encaminhado de imediato à reabilitação para nova profissão.",
    "Com prognóstico de retorno à atividade habitual, reabilitação não é indicada agora.")],
  "A incapacidade é avaliada em relação à atividade habitual (art. 59). Com prognóstico definido de recuperação, a incapacidade é temporária; a reabilitação (art. 62) é indicada quando o segurado é insuscetível de recuperação para a atividade habitual.",
  "Lei 8.213/1991, arts. 59, 62 e 86", "Antecipar consolidação ou reabilitação; confundir atividade habitual com qualquer atividade.")

q(Q, D, "Perícia médica previdenciária", "Reabilitação profissional", 3, SIT, C,
  "Motorista de caminhão com epilepsia refratária e crises mensais, apesar de tratamento otimizado, tem "
  "38 anos, ensino médio e boa capacidade cognitiva. Considerando a Lei nº 8.213/1991 e a avaliação "
  "pericial, assinale a afirmativa CORRETA.",
  "Há incapacidade para a atividade habitual sem perspectiva de retorno, sendo indicada reabilitação profissional para atividade sem risco.",
  [("Há incapacidade total e permanente para qualquer atividade, devendo ser concedida desde logo a aposentadoria.",
    "Jovem, escolarizado e sem déficit cognitivo: é suscetível de reabilitação para atividade sem risco."),
   ("Há capacidade plena para a atividade habitual, pois a epilepsia controlada parcialmente não impede a direção profissional.",
    "Crises mensais refratárias contraindicam direção profissional."),
   ("Há incapacidade temporária para a atividade habitual, devendo o benefício ser mantido até o controle total das crises.",
    "Refratariedade com tratamento otimizado afasta a perspectiva de retorno à direção."),
   ("Há incapacidade apenas para dirigir veículos leves, mantendo-se a aptidão para veículos de carga com acompanhante.",
    "O risco é maior na direção de veículos de carga.")],
  "Art. 62: o segurado em gozo de auxílio por incapacidade temporária, insuscetível de recuperação para sua atividade habitual, deverá submeter-se a processo de reabilitação profissional para outra atividade. A aposentadoria (art. 42) pressupõe impossibilidade de reabilitação para atividade que garanta a subsistência.",
  "Lei 8.213/1991, arts. 42 e 62", "Saltar da incapacidade para a atividade habitual direto para a aposentadoria.")

# ---------------------------------------------------------------- Doenças ocupacionais / nexo
q(Q, D, "Doenças ocupacionais e relacionadas ao trabalho", "Art. 20, § 1º – exclusões", 3, SIT, C,
  "Trabalhador rural de 61 anos, com gonartrose bilateral, requer reconhecimento de doença do trabalho. "
  "Não há registro de exposição específica que tenha contribuído diretamente para o agravo. Considerando "
  "a Lei nº 8.213/1991, assinale a afirmativa CORRETA.",
  "A doença degenerativa ou inerente a grupo etário não é doença do trabalho, salvo prova de contribuição direta do trabalho.",
  [("A doença degenerativa é sempre considerada doença do trabalho quando o segurado exerce atividade que exige esforço físico.",
    "O art. 20, § 1º, 'a' e 'b', exclui degenerativas e inerentes ao grupo etário."),
   ("A doença degenerativa nunca pode ter relação com o trabalho, sendo vedada a análise de concausa pelo perito.",
    "A concausa (art. 21, I) pode ser analisada quando o trabalho contribui diretamente."),
   ("A doença degenerativa é considerada doença profissional, por ser peculiar à atividade rural segundo o regulamento.",
    "Gonartrose não é doença profissional típica da atividade rural."),
   ("A doença degenerativa é considerada doença do trabalho quando gera incapacidade, independentemente de nexo com a atividade.",
    "Incapacidade não substitui o nexo.")],
  "Art. 20, § 1º: não são consideradas doença do trabalho a degenerativa, a inerente a grupo etário, a que não produza incapacidade laborativa e a endêmica (salvo exposição pela natureza do trabalho). O art. 21, I, equipara a acidente o agravo para o qual o trabalho contribuiu diretamente, ainda que não seja causa única (concausa).",
  "Lei 8.213/1991, arts. 20, § 1º, e 21, I", "Absolutos opostos: 'sempre' × 'nunca'.")

q(Q, D, "Doenças ocupacionais e relacionadas ao trabalho", "Doença endêmica", 3, SIT, C,
  "Agente de combate às endemias que realizava busca ativa em área de mata contraiu leishmaniose "
  "tegumentar, doença endêmica na região. Considerando o art. 20 da Lei nº 8.213/1991, assinale a "
  "afirmativa CORRETA.",
  "A doença endêmica pode ser doença do trabalho quando decorre de exposição determinada pela natureza do trabalho.",
  [("A doença endêmica nunca é considerada doença do trabalho, por ser adquirida por qualquer habitante da região.",
    "A lei ressalva a exposição ou contato direto determinado pela natureza do trabalho."),
   ("A doença endêmica é sempre considerada doença do trabalho para servidores públicos que atuam na região.",
    "O critério é a exposição pela natureza do trabalho, não o vínculo público."),
   ("A doença endêmica só é considerada doença do trabalho se constar da lista de doenças profissionais da CLT.",
    "A ressalva legal independe dessa lista."),
   ("A doença endêmica é considerada doença do trabalho desde que o trabalhador resida fora da área endêmica.",
    "O local de residência não é o critério.")],
  "Art. 20, § 1º, 'd': não é considerada doença do trabalho a doença endêmica adquirida por segurado habitante de região em que ela se desenvolva, salvo comprovação de que resultou de exposição ou contato direto determinado pela natureza do trabalho.",
  "Lei 8.213/1991, art. 20, § 1º, 'd'", "Regra geral apresentada sem a exceção legal.")

q(Q, D, "Nexo técnico epidemiológico", "NTEP – presunção e contestação", 3, SIT, C,
  "Bancária afastada por transtorno depressivo teve o benefício caracterizado como acidentário pelo NTEP, "
  "embora a empresa não tenha emitido CAT. A empresa discorda. Considerando o art. 21-A da Lei nº "
  "8.213/1991, assinale a afirmativa CORRETA.",
  "O NTEP gera presunção relativa, a partir do cruzamento CNAE × CID, que a empresa pode contestar com efeito suspensivo.",
  [("O NTEP gera presunção absoluta a partir da relação entre a atividade da empresa e o CID, sendo vedada qualquer contestação pela empresa.",
    "A presunção é relativa; a empresa pode requerer a não aplicação (§ 2º)."),
   ("O NTEP depende da emissão prévia da CAT pela empresa, sem a qual a perícia não pode caracterizar a natureza acidentária.",
    "O NTEP independe de CAT; decorre do cruzamento CNAE × CID."),
   ("O NTEP gera presunção relativa, mas o requerimento de não aplicação pela empresa não tem efeito suspensivo.",
    "O § 2º prevê efeito suspensivo."),
   ("O NTEP decorre da avaliação individual do posto de trabalho pelo perito, dispensando dados estatísticos de adoecimento.",
    "É nexo epidemiológico, fundado em dados estatísticos (CNAE × CID); a perícia pode afastá-lo no caso concreto.")],
  "Art. 21-A: a perícia médica do INSS considerará caracterizada a natureza acidentária quando constatar nexo técnico epidemiológico entre o trabalho e o agravo, decorrente da relação entre a atividade da empresa e a entidade mórbida (CID). § 1º: deixa de aplicar quando demonstrada a inexistência. § 2º: a empresa pode requerer a não aplicação, com efeito suspensivo, cabendo recurso ao CRPS.",
  "Lei 8.213/1991, art. 21-A; Decreto 3.048/1999, art. 337 e Anexo II, Lista C", "Absoluta × relativa; vincular NTEP à CAT.")

q(Q, D, "Doenças ocupacionais e relacionadas ao trabalho", "CAT – prazos e legitimados", 2, SIT, C,
  "Operário sofreu queda de andaime numa sexta-feira à tarde, sem óbito. A empresa não emitiu a CAT, "
  "e o médico que o atendeu no pronto-socorro pretende emiti-la. Considerando o art. 22 da Lei nº "
  "8.213/1991, assinale a afirmativa CORRETA.",
  "A empresa deveria comunicar até o primeiro dia útil seguinte; na falta, o médico assistente pode emitir a CAT, sem prazo.",
  [("A empresa deveria comunicar em até quinze dias; na sua falta, apenas o próprio acidentado pode emitir a CAT, observado igual prazo.",
    "O prazo é o primeiro dia útil seguinte; vários legitimados podem emitir, sem prazo."),
   ("A empresa deveria comunicar de imediato; na sua falta, o médico assistente fica impedido de emitir a CAT por sigilo profissional.",
    "Imediata é a comunicação em caso de morte; o médico assistente é legitimado."),
   ("A empresa deveria comunicar até o primeiro dia útil seguinte; na sua falta, a CAT só pode ser emitida por ordem judicial.",
    "O § 2º legitima acidentado, dependentes, sindicato, médico e autoridade pública."),
   ("A empresa deveria comunicar até o primeiro dia útil seguinte; na sua falta, o sindicato pode emitir a CAT em até 48 horas.",
    "Os demais legitimados não estão sujeitos a esse prazo.")],
  "Art. 22: a empresa comunicará o acidente à Previdência até o 1º dia útil seguinte ao da ocorrência e, em caso de morte, de imediato. § 2º: na falta, podem formalizá-la o acidentado, seus dependentes, a entidade sindical, o médico que o assistiu ou qualquer autoridade pública, não prevalecendo o prazo.",
  "Lei 8.213/1991, art. 22", "Troca de prazos e de legitimados.")

q(Q, D, "Avaliação de dano corporal e nexo causal", "Critérios de nexo causal", 3, SIT, C,
  "Em perícia judicial cível, o autor atribui lombociatalgia crônica a colisão traseira de baixa "
  "energia ocorrida há dois anos; exames anteriores ao evento já mostravam discopatia multinível. "
  "Considerando os critérios médico-legais de nexo causal, assinale a afirmativa CORRETA.",
  "O nexo exige adequação entre trauma e lesão, coerência topográfica e cronológica e exclusão de causa estranha.",
  [("O nexo exige apenas a relação cronológica entre o evento e o início dos sintomas, sendo dispensável a análise do estado anterior.",
    "Cronologia isolada não basta; o estado anterior é central."),
   ("O nexo é presumido sempre que o periciando apresenta exame de imagem alterado após o evento traumático alegado.",
    "Alteração posterior pode ser preexistente/degenerativa."),
   ("O nexo exige adequação entre trauma e lesão, sendo a existência de doença prévia suficiente, por si só, para afastá-lo.",
    "Estado anterior pode configurar concausa ou agravamento; não afasta automaticamente."),
   ("O nexo é estabelecido pelo relato do periciando, cabendo ao perito apenas quantificar o dano decorrente do evento.",
    "O nexo é conclusão técnica do perito, não do relato.")],
  "Critérios clássicos (Simonin / Muller-Cordonnier): natureza adequada do traumatismo e da lesão, adequação entre sede do trauma e da lesão, encadeamento anatomoclínico, adequação temporal, exclusão de causa estranha e consideração do estado anterior.",
  "Medicina Legal – avaliação do dano corporal (critérios de nexo de causalidade)", "'Por si só' e 'apenas' em critérios cumulativos.")

q(Q, D, "Avaliação de dano corporal e nexo causal", "Concausas", 2, DIR, C,
  "Na avaliação do dano corporal, o perito frequentemente identifica fatores que concorrem com o evento "
  "principal para o resultado. Assinale a afirmativa CORRETA sobre as concausas.",
  "As concausas podem ser preexistentes, concomitantes ou supervenientes, sem afastar necessariamente o nexo com o evento.",
  [("As concausas são sempre preexistentes ao evento e, quando presentes, afastam o nexo entre o evento e o resultado.",
    "Podem ser preexistentes, concomitantes ou supervenientes, e não afastam necessariamente o nexo."),
   ("As concausas são sempre supervenientes ao evento e transferem integralmente a responsabilidade pelo resultado a terceiros.",
    "Não são só supervenientes nem transferem automaticamente a responsabilidade."),
   ("As concausas restringem-se a fatores patológicos do periciando, excluídos fatores externos como infecção hospitalar.",
    "Fatores externos supervenientes (ex.: infecção) podem ser concausas."),
   ("As concausas só são relevantes no âmbito penal, sendo desconsideradas na perícia previdenciária e trabalhista.",
    "No acidentário, o art. 21, I, da Lei 8.213 trata da concausalidade.")],
  "Concausa é fator que, somado à causa principal, concorre para o resultado; classifica-se em preexistente, concomitante ou superveniente. Na Lei 8.213 (art. 21, I), o trabalho que contribuiu diretamente, sem ser causa única, caracteriza acidente.",
  "Medicina Legal; Lei 8.213/1991, art. 21, I", "'Sempre' e 'restringem-se'.")

# ---------------------------------------------------------------- BPC
q(Q, D, "Perícia médica previdenciária", "BPC – deficiência × incapacidade", 3, SIT, C,
  "Criança de 6 anos com transtorno do espectro autista, com necessidade de suporte substancial na "
  "comunicação e nas atividades diárias, tem pedido de BPC. Considerando a Lei nº 8.742/1993 (LOAS), "
  "assinale a afirmativa CORRETA.",
  "A avaliação verifica impedimento de longo prazo em interação com barreiras, sem exigir incapacidade para o trabalho.",
  [("A avaliação verifica incapacidade para o trabalho e para a vida independente, sendo inviável o benefício a menores de 16 anos.",
    "O conceito vigente é de impedimento de longo prazo em interação com barreiras; crianças podem receber."),
   ("A avaliação verifica impedimento de curto prazo, bastando a duração mínima de seis meses para a concessão do benefício.",
    "Longo prazo é de no mínimo dois anos (art. 20, § 10)."),
   ("A avaliação verifica impedimento de longo prazo, sendo realizada exclusivamente pela perícia médica, sem avaliação social.",
    "A avaliação é médica e social (art. 20, § 6º)."),
   ("A avaliação verifica impedimento de longo prazo, dispensando-se a análise da renda familiar quando o diagnóstico é confirmado.",
    "O critério de renda continua exigido.")],
  "Art. 20, § 2º: pessoa com deficiência é aquela com impedimento de longo prazo de natureza física, mental, intelectual ou sensorial que, em interação com uma ou mais barreiras, pode obstruir sua participação plena e efetiva na sociedade. § 10: longo prazo = mínimo de 2 anos. § 6º: avaliação médica e social.",
  "Lei 8.742/1993, art. 20, §§ 2º, 6º e 10", "Confundir incapacidade laboral (RGPS) com deficiência (BPC).")

q(Q, D, "Perícia médica previdenciária", "BPC – requisitos", 2, DIR, C,
  "Considerando o Benefício de Prestação Continuada previsto no art. 20 da Lei nº 8.742/1993, assinale a "
  "afirmativa CORRETA.",
  "O benefício garante um salário mínimo à pessoa com deficiência e ao idoso de 65 anos ou mais sem meios de se manter.",
  [("O benefício garante um salário mínimo à pessoa com deficiência e ao idoso com 60 anos ou mais, exigida contribuição prévia ao RGPS.",
    "A idade é 65 anos e não há exigência de contribuição (benefício assistencial)."),
   ("O benefício garante meio salário mínimo à pessoa com deficiência e ao idoso com 65 anos ou mais, cumulável com aposentadoria.",
    "O valor é de um salário mínimo e, em regra, não é cumulável com outro benefício da seguridade."),
   ("O benefício garante um salário mínimo ao idoso com 65 anos ou mais, sendo a pessoa com deficiência atendida pelo RGPS.",
    "A pessoa com deficiência é destinatária do BPC."),
   ("O benefício garante um salário mínimo à pessoa com deficiência, desde que comprovada incapacidade total para os atos da vida civil.",
    "Não se exige incapacidade civil; exige-se impedimento de longo prazo.")],
  "Art. 20: o BPC é a garantia de um salário mínimo mensal à pessoa com deficiência e ao idoso com 65 anos ou mais que comprovem não possuir meios de prover a própria manutenção nem de tê-la provida por sua família.",
  "Lei 8.742/1993, art. 20", "Troca de idade (60 × 65) e exigência de contribuição.")

# ---------------------------------------------------------------- Ética pericial
q(Q, D, "Bioética aplicada à perícia médica", "CEM – perito do próprio paciente", 2, SIT, C,
  "Perita médica do município é designada para avaliar servidor que ela acompanhou como psiquiatra "
  "assistente no ano anterior. Considerando o Código de Ética Médica (Res. CFM nº 2.217/2018), assinale "
  "a afirmativa CORRETA.",
  "É vedado ao médico ser perito de seu próprio paciente, devendo a perita declarar-se impedida para a avaliação.",
  [("É permitido ao médico ser perito de seu próprio paciente, pois o conhecimento prévio do caso aumenta a precisão do laudo.",
    "O art. 93 veda expressamente."),
   ("É permitido ao médico ser perito de seu próprio paciente, desde que o periciando concorde por escrito com a avaliação.",
    "A concordância do periciando não afasta a vedação."),
   ("É vedado ao médico ser perito de seu próprio paciente apenas na perícia judicial, sendo permitido na perícia administrativa.",
    "A vedação ética alcança qualquer função pericial."),
   ("É vedado ao médico ser perito de seu próprio paciente apenas enquanto mantido o tratamento, cessando a vedação após a alta.",
    "A relação assistencial prévia compromete a isenção; o caso exige declarar-se impedida.")],
  "Art. 93: é vedado ao médico ser perito ou auditor do próprio paciente, de pessoa de sua família ou de qualquer outra com a qual tenha relações capazes de influir em seu trabalho ou de empresa em que atue ou tenha atuado.",
  "Res. CFM 2.217/2018 (CEM), art. 93", "Condicionantes falsas ('desde que concorde', 'apenas na judicial').")

q(Q, D, "Bioética aplicada à perícia médica", "CEM – laudo sem exame pessoal", 2, SIT, C,
  "Por sobrecarga de agenda, um perito pretende assinar laudos elaborados por médico residente que "
  "examinou os periciandos, sem reexaminá-los. Considerando o Código de Ética Médica, assinale a "
  "afirmativa CORRETA.",
  "É vedado ao médico assinar laudos periciais quando não tenha realizado pessoalmente o exame.",
  [("É permitido ao médico assinar laudos periciais elaborados por terceiro, desde que este seja médico regularmente inscrito no CRM.",
    "O art. 92 exige exame pessoal de quem assina."),
   ("É permitido ao médico assinar laudos periciais sem exame pessoal quando houver documentação médica suficiente nos autos.",
    "Documentos não substituem o exame pessoal para quem assina o laudo."),
   ("É vedado ao médico assinar laudos periciais sem exame pessoal apenas nas perícias criminais de corpo de delito.",
    "A vedação alcança laudos periciais, auditoriais e de verificação médico-legal em geral."),
   ("É permitido ao médico assinar laudos periciais sem exame pessoal, desde que a autoridade requisitante autorize por escrito.",
    "A autorização da autoridade não afasta a vedação ética.")],
  "Art. 92: é vedado ao médico assinar laudos periciais, auditoriais ou de verificação médico-legal caso não tenha realizado pessoalmente o exame.",
  "Res. CFM 2.217/2018 (CEM), art. 92", "'Desde que' legitimando conduta vedada.")

q(Q, D, "Bioética aplicada à perícia médica", "CEM – modificar tratamento", 3, SIT, C,
  "Durante perícia, a perita constata que o periciando usa dose de lítio potencialmente tóxica, com "
  "tremor grosseiro e confusão mental. Considerando o Código de Ética Médica, assinale a afirmativa "
  "CORRETA.",
  "Em regra é vedado ao perito modificar o tratamento, salvo urgência, comunicando o fato por escrito ao médico assistente.",
  [("É sempre vedado ao perito modificar o tratamento, devendo limitar-se a registrar o achado no laudo, sem outra providência.",
    "O art. 97 ressalva urgência, emergência e iminente perigo de morte."),
   ("É permitido ao perito modificar livremente o tratamento, pois sua função inclui a correção de condutas do médico assistente.",
    "A regra é a vedação; a exceção é a urgência."),
   ("É vedado ao perito modificar o tratamento, mas pode suspender o benefício até que o periciando ajuste a medicação.",
    "Não há base para suspender o benefício nesse contexto; o caso é de urgência clínica."),
   ("Em regra é vedado ao perito modificar o tratamento, mas pode fazê-lo em urgência, dispensada a comunicação ao médico assistente.",
    "A comunicação por escrito ao médico assistente é exigida.")],
  "Art. 97: é vedado ao médico autorizar, vetar, bem como modificar, quando na função de auditor ou de perito, procedimentos propedêuticos ou terapêuticos instituídos, salvo, no último caso, em situações de urgência, emergência ou iminente perigo de morte do paciente, comunicando, por escrito, o fato ao médico assistente.",
  "Res. CFM 2.217/2018 (CEM), art. 97", "Absoluto ('sempre vedado') e supressão do dever de comunicar.")

q(Q, D, "Bioética aplicada à perícia médica", "CEM – conduta durante o exame", 2, DIR, I,
  "Considerando as vedações do Capítulo XI (Auditoria e Perícia Médica) do Código de Ética Médica, "
  "assinale a afirmativa INCORRETA.",
  "É permitido ao perito comentar, diante do examinado, erros do médico assistente.",
  [("É vedado ao perito receber remuneração vinculada ao sucesso da causa.",
    "Correta: art. 96."),
   ("É vedado ao perito deixar de atuar com absoluta isenção quando designado para a função.",
    "Correta: art. 98."),
   ("É vedado ao perito ultrapassar os limites de suas atribuições e de sua competência.",
    "Correta: art. 98."),
   ("É vedado ao perito assinar laudo sem ter realizado pessoalmente o exame.",
    "Correta: art. 92.")],
  "Art. 94: é vedado ao médico intervir, quando em função de auditor, assistente técnico ou perito, nos atos profissionais de outro médico, ou fazer qualquer apreciação em presença do examinado, reservando suas observações para o relatório.",
  "Res. CFM 2.217/2018 (CEM), arts. 92, 94, 96 e 98", "Comando INCORRETA: as demais são literalidade do CEM.")

# ---------------------------------------------------------------- CPC
q(Q, D, "Bioética aplicada à perícia médica", "CPC – assistente técnico", 3, SIT, C,
  "Em perícia judicial previdenciária, o assistente técnico do INSS foi indicado e a parte autora "
  "alegou que ele seria suspeito por ser servidor da autarquia. Considerando o CPC, assinale a "
  "afirmativa CORRETA.",
  "Os assistentes técnicos são de confiança da parte e não se sujeitam a impedimento ou suspeição.",
  [("Os assistentes técnicos sujeitam-se às mesmas causas de impedimento e suspeição do perito, devendo ser substituídos no caso.",
    "O art. 466, § 1º, afasta impedimento e suspeição dos assistentes."),
   ("Os assistentes técnicos são de confiança do juízo e, por isso, devem ser escolhidos entre peritos cadastrados no tribunal.",
    "São de confiança da parte."),
   ("Os assistentes técnicos são de confiança da parte, mas o perito pode realizar as diligências sem lhes dar ciência prévia.",
    "O art. 466, § 2º, exige comunicação prévia com antecedência mínima de 5 dias."),
   ("Os assistentes técnicos são de confiança da parte e assinam o laudo em conjunto com o perito, que o subscreve como revisor.",
    "O assistente apresenta parecer próprio; o laudo é do perito.")],
  "Art. 466, § 1º: os assistentes técnicos são de confiança da parte e não estão sujeitos a impedimento ou suspeição. § 2º: o perito deve assegurar aos assistentes o acesso e o acompanhamento das diligências, com prévia comunicação, comprovada nos autos, com antecedência mínima de 5 dias.",
  "CPC, art. 466, §§ 1º e 2º", "Estender ao assistente regras do perito.")

q(Q, D, "Bioética aplicada à perícia médica", "CPC – limites do laudo", 2, SIT, C,
  "No laudo de perícia judicial sobre incapacidade, a perita acrescentou opinião sobre a 'má-fé' do "
  "autor e sugeriu ao juiz a improcedência do pedido. Considerando o art. 473 do CPC, assinale a "
  "afirmativa CORRETA.",
  "É vedado ao perito ultrapassar os limites da designação e emitir opiniões pessoais alheias ao exame técnico.",
  [("É dever do perito indicar ao juiz a solução jurídica do pedido, por ser o profissional com conhecimento técnico do caso.",
    "A solução jurídica cabe ao juiz; o perito responde ao objeto técnico."),
   ("É permitido ao perito emitir opiniões pessoais sobre a conduta das partes, desde que fundamente em linguagem simples.",
    "O § 2º veda opiniões pessoais que excedam o exame técnico."),
   ("É vedado ao perito responder a quesitos das partes, devendo limitar-se aos quesitos formulados pelo juiz.",
    "O laudo deve responder conclusivamente a todos os quesitos (art. 473, IV)."),
   ("É permitido ao perito ampliar o objeto da perícia quando identificar fatos relevantes, dispensando autorização do juízo.",
    "Ultrapassar os limites da designação é vedado.")],
  "Art. 473, § 2º: é vedado ao perito ultrapassar os limites de sua designação, bem como emitir opiniões pessoais que excedam o exame técnico ou científico do objeto da perícia. Inciso IV: resposta conclusiva a todos os quesitos apresentados pelo juiz, pelas partes e pelo MP.",
  "CPC, art. 473, IV e § 2º", "Confundir conclusão técnica com conclusão jurídica.")

q(Q, D, "Bioética aplicada à perícia médica", "CPC – valoração do laudo", 2, DIR, C,
  "Considerando a valoração da prova pericial pelo juiz, conforme o CPC, assinale a afirmativa CORRETA.",
  "O juiz não está adstrito ao laudo, mas deve fundamentar por que acolhe ou afasta suas conclusões.",
  [("O juiz está vinculado às conclusões do laudo, só podendo afastá-las mediante a realização de nova perícia.",
    "O juiz aprecia a prova livremente, com fundamentação (art. 479)."),
   ("O juiz não está adstrito ao laudo e pode afastá-lo sem fundamentação, em razão do livre convencimento.",
    "O art. 479 exige indicação dos motivos."),
   ("O juiz está vinculado ao laudo quando não houver impugnação das partes no prazo legal.",
    "A ausência de impugnação não vincula o juiz."),
   ("O juiz não está adstrito ao laudo, mas é vedada a determinação de nova perícia sobre a mesma matéria.",
    "O art. 480 admite nova perícia quando a matéria não estiver suficientemente esclarecida.")],
  "Art. 479: o juiz apreciará a prova pericial de acordo com o art. 371, indicando na sentença os motivos que o levaram a considerar ou a deixar de considerar as conclusões do laudo. Art. 480: nova perícia quando a matéria não estiver suficientemente esclarecida.",
  "CPC, arts. 371, 479 e 480", "Vinculação × livre convencimento sem motivação.")

q(Q, D, "Bioética aplicada à perícia médica", "CPC – escusa do perito", 3, DIR, C,
  "Médica nomeada perita judicial constatou que é vizinha e amiga íntima do autor. Considerando o CPC, "
  "assinale a afirmativa CORRETA.",
  "A escusa deve ser apresentada em 15 dias da intimação ou da suspeição superveniente, sob pena de renúncia.",
  [("A escusa deve ser apresentada no prazo de 5 dias, contado da entrega do laudo, sob pena de nulidade da perícia realizada.",
    "O prazo é de 15 dias, contado da intimação, da suspeição ou do impedimento supervenientes."),
   ("A escusa pode ser apresentada a qualquer tempo, inclusive após a entrega do laudo, sem consequência processual.",
    "Há prazo, sob pena de renúncia."),
   ("A escusa é dispensada, pois amizade íntima com a parte não configura suspeição aplicável ao perito.",
    "As causas de suspeição do juiz aplicam-se ao perito (art. 148, II), incluindo amizade íntima."),
   ("A escusa deve ser apresentada no prazo de 15 dias, mas somente nos casos de impedimento, sendo vedada por suspeição.",
    "Cabe escusa por impedimento ou suspeição.")],
  "Art. 157, § 1º: a escusa será apresentada no prazo de 15 dias, contado da intimação, da suspeição ou do impedimento supervenientes, sob pena de renúncia ao direito a alegá-la. Art. 148, II, e art. 145, I: amizade íntima é causa de suspeição aplicável ao perito.",
  "CPC, arts. 145, 148, II, e 157, § 1º", "Troca de prazo e de termo inicial.")

# ---------------------------------------------------------------- Clínica pericial
q(Q, D, "Exame clínico direcionado à perícia médica", "Sinais de Waddell", 3, SIT, C,
  "Periciando com lombalgia crônica apresenta dor à compressão axial do crânio, à rotação simulada do "
  "tronco, Lasègue positivo deitado e negativo sentado, e reação exagerada ao exame. Considerando os "
  "sinais de Waddell, assinale a afirmativa CORRETA.",
  "A positividade de três ou mais categorias sugere componente não orgânico, mas não comprova simulação por si só.",
  [("A positividade de três ou mais categorias comprova simulação, autorizando a conclusão de capacidade plena no laudo.",
    "Os sinais indicam componente não orgânico/comportamental; não diagnosticam simulação."),
   ("A positividade de qualquer um dos sinais basta para afastar doença orgânica da coluna lombar.",
    "Um sinal isolado tem baixo valor; a interpretação considera três ou mais categorias."),
   ("A positividade de três ou mais categorias indica radiculopatia orgânica, devendo ser confirmada por eletroneuromiografia.",
    "Os sinais de Waddell não indicam radiculopatia."),
   ("A positividade dos sinais deve ser desconsiderada, pois sua aplicação é vedada na perícia previdenciária.",
    "Não há essa vedação; são ferramenta semiológica auxiliar.")],
  "Os sinais de Waddell (sensibilidade, simulação, distração, distúrbios regionais e reação exagerada) indicam componente não orgânico quando positivos em três ou mais das cinco categorias; não diferenciam simulação de fatores psicossociais.",
  "Waddell et al., Spine 1980 – semiologia pericial", "Equiparar 'não orgânico' a 'simulação'.")

q(Q, D, "Exame clínico direcionado à perícia médica", "Sinal de Hoover", 3, SIT, C,
  "Periciando refere paresia do membro inferior direito. Ao fletir ativamente o quadril esquerdo contra "
  "resistência, a perita sente extensão vigorosa do quadril direito, que antes parecia sem força. "
  "Considerando a semiologia pericial, assinale a afirmativa CORRETA.",
  "O achado corresponde ao sinal de Hoover positivo, sugestivo de fraqueza funcional do membro referido.",
  [("O achado corresponde ao sinal de Babinski, sugestivo de lesão do neurônio motor superior no membro referido.",
    "Babinski é reflexo cutâneo-plantar; o achado descrito é o teste de Hoover."),
   ("O achado corresponde ao sinal de Hoover positivo, indicativo de lesão radicular L5 no membro referido.",
    "Hoover positivo sugere componente funcional, não radiculopatia."),
   ("O achado corresponde ao sinal de Romberg, sugestivo de comprometimento da sensibilidade proprioceptiva.",
    "Romberg avalia equilíbrio com olhos fechados."),
   ("O achado corresponde ao sinal de Hoover negativo, confirmando a paresia orgânica do membro referido.",
    "A extensão involuntária presente torna o sinal positivo para componente funcional.")],
  "No teste de Hoover, a flexão do quadril contralateral contra resistência provoca extensão involuntária do quadril 'parético'. Força presente nessa manobra, ausente no teste direto, sugere fraqueza funcional.",
  "Semiologia neurológica aplicada à perícia", "Troca de epônimos e de interpretação (positivo × negativo).")

q(Q, D, "Avaliação pericial em doenças psiquiátricas", "Diagnóstico × incapacidade", 2, SIT, C,
  "Professora com episódio depressivo moderado (CID-10 F32.1), em tratamento há três semanas, apresenta "
  "lentificação, prejuízo de concentração e insônia, com ideação passiva de morte. Considerando a "
  "avaliação pericial psiquiátrica, assinale a afirmativa CORRETA.",
  "A incapacidade decorre da repercussão funcional dos sintomas sobre a atividade, e não do diagnóstico isolado.",
  [("A incapacidade decorre do diagnóstico de episódio depressivo, que por si só gera afastamento de no mínimo um ano.",
    "Diagnóstico não equivale a incapacidade; não há prazo mínimo legal."),
   ("A incapacidade deve ser negada, pois o tratamento iniciado há três semanas indica boa adesão e controle dos sintomas.",
    "Três semanas é tempo inicial; o quadro descrito tem repercussão funcional relevante."),
   ("A incapacidade decorre da gravidade do CID informado no atestado, que vincula a conclusão do perito.",
    "O atestado do assistente não vincula o perito."),
   ("A incapacidade deve ser considerada permanente, pois transtornos depressivos têm curso crônico e recorrente.",
    "Episódio moderado em tratamento inicial tem prognóstico de recuperação: temporária.")],
  "Na perícia, a incapacidade é inferida da repercussão funcional (sintomas, exame psíquico, gravidade, adesão e tempo de tratamento) frente às exigências da atividade; o diagnóstico isolado não define incapacidade nem sua duração.",
  "Diretrizes de perícia médica (INSS) – transtornos mentais", "'Por si só' e 'vincula'.")

q(Q, D, "Classificação Internacional de Doenças (CID-10/CID-11)", "Burnout na CID-11", 3, DIR, C,
  "A síndrome de burnout tem sido frequentemente alegada em perícias de servidores. Considerando sua "
  "classificação na CID-11, assinale a afirmativa CORRETA.",
  "Na CID-11, o burnout (QD85) é fenômeno ocupacional, no capítulo de fatores que influenciam a saúde, e não transtorno mental.",
  [("Na CID-11, o burnout é classificado como transtorno depressivo, no capítulo de transtornos mentais, com código iniciado por 6A.",
    "O burnout não está no capítulo 06; o código é QD85."),
   ("Na CID-11, o burnout é descrito como fenômeno ocupacional aplicável a qualquer contexto de vida, inclusive o familiar.",
    "A definição restringe-se ao contexto ocupacional."),
   ("Na CID-11, o burnout é classificado como transtorno de ansiedade, exigindo exclusão de causas orgânicas para o diagnóstico.",
    "Não é classificado como transtorno de ansiedade."),
   ("Na CID-11, o burnout foi excluído da classificação, por ausência de critérios diagnósticos operacionais.",
    "Consta como QD85.")],
  "Na CID-11 (vigente na OMS desde 01/01/2022), 'burn-out' (QD85) integra o capítulo 'Fatores que influenciam o estado de saúde ou o contato com serviços de saúde', definido como fenômeno ocupacional resultante de estresse crônico no trabalho não gerenciado com sucesso.",
  "OMS – CID-11, QD85", "Classificar como transtorno mental ou ampliar para contextos não ocupacionais.")

q(Q, D, "Avaliação pericial em doenças osteomusculares", "Túnel do carpo", 2, SIT, C,
  "Digitadora relata parestesias noturnas em polegar, indicador e médio da mão direita; Phalen e Tinel "
  "no punho são positivos e há hipotrofia tenar discreta. Considerando a avaliação pericial, assinale a "
  "afirmativa CORRETA.",
  "O quadro sugere síndrome do túnel do carpo, cuja confirmação e graduação se fazem pela eletroneuromiografia.",
  [("O quadro sugere síndrome do túnel cubital, cuja confirmação se faz pela radiografia simples do cotovelo direito.",
    "A distribuição é mediana (polegar, indicador e médio) e os testes são no punho."),
   ("O quadro sugere síndrome do túnel do carpo, sendo o diagnóstico pericial dispensável de correlação com exames complementares.",
    "A ENMG confirma e gradua; a correlação clínico-complementar é recomendada."),
   ("O quadro sugere radiculopatia C8, cuja confirmação se faz pela ressonância magnética da coluna cervical.",
    "C8 acomete 4º e 5º dedos; o quadro é do nervo mediano."),
   ("O quadro sugere síndrome do túnel do carpo, cuja hipotrofia tenar indica fase inicial e reversível sem tratamento.",
    "Hipotrofia tenar indica comprometimento mais avançado (axonal).")],
  "Parestesias no território do mediano, Phalen e Tinel no punho e hipotrofia tenar sugerem STC; a eletroneuromiografia confirma e gradua o comprometimento.",
  "Semiologia ortopédica/neurológica; DORT", "Troca de território nervoso e de estadiamento.")

q(Q, D, "Doenças ocupacionais e relacionadas ao trabalho", "PAIR", 3, DIR, C,
  "Considerando as características da perda auditiva induzida por ruído (PAIR) ocupacional, assinale a "
  "afirmativa CORRETA.",
  "A PAIR é neurossensorial, bilateral e simétrica, irreversível, com entalhe em 3, 4 ou 6 kHz, e não progride sem exposição.",
  [("A PAIR é condutiva, em geral unilateral, reversível, com predomínio nas frequências graves, e progride após cessar a exposição.",
    "É neurossensorial, bilateral, irreversível, com predomínio em agudos; não progride sem exposição."),
   ("A PAIR é neurossensorial, em geral bilateral e simétrica, mas continua progredindo indefinidamente após cessar a exposição.",
    "Cessada a exposição, a PAIR não progride."),
   ("A PAIR é neurossensorial, em geral bilateral, com entalhe nas frequências de 250 e 500 Hz, poupando as frequências agudas.",
    "O entalhe típico ocorre em 3, 4 ou 6 kHz."),
   ("A PAIR é mista, em geral assimétrica, com reversão completa em até seis meses de afastamento do ruído.",
    "É neurossensorial e irreversível.")],
  "PAIR: perda neurossensorial, quase sempre bilateral e simétrica, irreversível, com entalhe em 3, 4 ou 6 kHz e recuperação em 8 kHz; não progride após cessada a exposição; raramente ultrapassa 40 dB nas frequências baixas e 75 dB nas altas.",
  "Ministério da Saúde – Perda Auditiva Induzida por Ruído (Protocolo); NR-7", "Troca condutiva × neurossensorial; progressão sem exposição.")

q(Q, D, "Avaliação pericial em doenças respiratórias", "Espirometria", 2, SIT, C,
  "Em perícia de ex-marmorista, a espirometria mostra CVF de 62% do previsto e VEF1/CVF de 0,86. "
  "Considerando a interpretação funcional respiratória, assinale a afirmativa CORRETA.",
  "O padrão sugere distúrbio restritivo, a ser confirmado pela medida da capacidade pulmonar total.",
  [("O padrão confirma distúrbio obstrutivo grave, pois a relação VEF1/CVF elevada indica limitação ao fluxo aéreo.",
    "Obstrução se caracteriza por VEF1/CVF REDUZIDA."),
   ("O padrão confirma distúrbio restritivo, sendo dispensável a medida da capacidade pulmonar total.",
    "A espirometria sugere; a CPT confirma a restrição."),
   ("O padrão é normal, pois a relação VEF1/CVF acima de 0,70 afasta qualquer distúrbio ventilatório.",
    "Relação normal não afasta restrição com CVF reduzida."),
   ("O padrão sugere distúrbio misto, pois a CVF reduzida associada à relação elevada define obstrução e restrição.",
    "Distúrbio misto exige relação reduzida com CVF reduzida e restrição confirmada.")],
  "CVF reduzida com VEF1/CVF normal ou elevada sugere distúrbio ventilatório restritivo, que deve ser confirmado pela redução da capacidade pulmonar total (pletismografia ou diluição de gases). Contexto compatível com silicose.",
  "Diretrizes SBPT para testes de função pulmonar", "Interpretar relação elevada como obstrução; 'dispensável'.")

q(Q, D, "Avaliação pericial em doenças cardiovasculares", "Cardiopatia grave", 3, SIT, C,
  "Segurado com cardiopatia isquêmica, fração de ejeção de 30% e dispneia aos pequenos esforços (classe "
  "funcional III da NYHA) requer benefício com isenção de carência. Considerando a avaliação pericial, "
  "assinale a afirmativa CORRETA.",
  "A caracterização de cardiopatia grave apoia-se em critérios funcionais e prognósticos, e não no diagnóstico isolado.",
  [("A caracterização de cardiopatia grave decorre do diagnóstico de doença isquêmica, independentemente da repercussão funcional.",
    "O diagnóstico isolado não define gravidade."),
   ("A caracterização de cardiopatia grave exige cirurgia cardíaca prévia, sem a qual não há enquadramento para isenção.",
    "Não há essa exigência."),
   ("A caracterização de cardiopatia grave depende apenas da idade do segurado, aplicando-se a partir dos 60 anos.",
    "Idade não é critério de gravidade cardíaca."),
   ("A caracterização de cardiopatia grave é atribuição do cardiologista assistente, cujo atestado vincula o perito.",
    "A caracterização é pericial; o atestado não vincula.")],
  "Cardiopatia grave é conceito médico-pericial baseado em limitação funcional (ex.: NYHA III–IV), disfunção ventricular (ex.: FE reduzida), isquemia, arritmias graves e prognóstico — não no rótulo diagnóstico.",
  "Lei 8.213/1991, art. 151; consenso de cardiopatia grave (SBC) – critérios funcionais", "Diagnóstico ou atestado tratados como suficientes.", verificar=True)

q(Q, D, "Avaliação pericial em doenças infecciosas", "HIV – estigma (Súmula 78 TNU)", 3, SIT, C,
  "Segurado com HIV, assintomático, carga viral indetectável, trabalhava como cozinheiro em pequena "
  "cidade, onde relata discriminação após a revelação do diagnóstico. Considerando a avaliação de "
  "incapacidade no âmbito judicial, assinale a afirmativa CORRETA.",
  "Além da condição clínica, devem ser consideradas as condições pessoais, sociais, econômicas e culturais do segurado.",
  [("A ausência de sintomas e a carga viral indetectável afastam qualquer análise de incapacidade, sendo irrelevante o contexto social.",
    "A Súmula 78 da TNU manda considerar o contexto social em face do estigma."),
   ("O diagnóstico de HIV gera presunção absoluta de incapacidade total e permanente, dispensando o exame pericial.",
    "Não há presunção absoluta; a análise é individual."),
   ("A ocupação de cozinheiro é incompatível com o HIV por risco de transmissão alimentar, gerando incapacidade técnica.",
    "Não há transmissão do HIV por manipulação de alimentos."),
   ("Além da condição clínica, deve ser considerada apenas a escolaridade, sendo o estigma social matéria estranha à perícia.",
    "A análise ampla inclui o estigma, conforme a súmula.")],
  "Súmula 78 da TNU: comprovado que o requerente é portador do HIV, cabe ao julgador verificar as condições pessoais, sociais, econômicas e culturais, de forma a analisar a incapacidade em sentido amplo, em face da elevada estigmatização social da doença.",
  "TNU, Súmula 78", "Restringir a análise ao quadro clínico; mito de transmissão alimentar.")

q(Q, D, "Medicina baseada em evidências", "Valor preditivo positivo", 3, SIT, C,
  "Um teste de rastreio tem sensibilidade de 90% e especificidade de 80% e foi aplicado em população "
  "com prevalência de 10% da doença. Considerando os conceitos de epidemiologia clínica, assinale a "
  "afirmativa CORRETA.",
  "O valor preditivo positivo é de aproximadamente 33%, pois depende também da prevalência da doença.",
  [("O valor preditivo positivo é de 90%, pois corresponde à sensibilidade do teste, independentemente da prevalência.",
    "Sensibilidade ≠ VPP; VPP = 0,09 ÷ (0,09 + 0,18) ≈ 33%."),
   ("O valor preditivo positivo é de 80%, pois corresponde à especificidade do teste na população estudada.",
    "Especificidade ≠ VPP."),
   ("O valor preditivo positivo é de aproximadamente 33%, e aumentaria caso a prevalência da doença fosse menor.",
    "Com prevalência menor, o VPP diminui."),
   ("O valor preditivo positivo é de aproximadamente 67%, pois resulta da média entre sensibilidade e especificidade.",
    "Não se calcula por média.")],
  "Em 1.000 pessoas: 100 doentes → 90 VP; 900 sadios → 180 FP (20%). VPP = 90 ÷ (90 + 180) ≈ 33%. O VPP cai quando a prevalência cai.",
  "Epidemiologia clínica – testes diagnósticos", "Confundir sensibilidade/especificidade com valores preditivos.")

q(Q, D, "Epidemiologia clínica aplicada à perícia", "Medidas de associação", 2, DIR, C,
  "Em estudo de caso-controle sobre exposição ocupacional à sílica e câncer de pulmão, os pesquisadores "
  "precisam estimar a associação. Considerando os desenhos epidemiológicos, assinale a afirmativa CORRETA.",
  "No estudo de caso-controle, a medida de associação adequada é a razão de chances, pois não se calcula a incidência.",
  [("No estudo de caso-controle, a medida de associação adequada é o risco relativo, calculado a partir da incidência nos expostos.",
    "O caso-controle parte do desfecho; não permite calcular incidência."),
   ("No estudo de caso-controle, a medida de associação adequada é a prevalência, obtida em um único momento no tempo.",
    "Prevalência é medida de frequência, típica de estudo transversal."),
   ("No estudo de caso-controle, a medida de associação adequada é o número necessário para tratar, derivado da redução de risco.",
    "NNT deriva de ensaios/coortes."),
   ("No estudo de caso-controle, a medida de associação adequada é a razão de chances, que sempre equivale exatamente ao risco relativo.",
    "Aproxima-se do RR apenas quando a doença é rara.")],
  "Caso-controle seleciona por desfecho; estima-se a OR. Em doenças raras a OR aproxima-se do RR. Coortes permitem incidência e RR.",
  "Epidemiologia clínica – desenhos de estudo", "'Sempre equivale' e troca de medidas.")

q(Q, D, "Medicina baseada em evidências", "Hierarquia de evidências", 1, DIR, C,
  "Considerando a hierarquia de níveis de evidência em medicina baseada em evidências para questões de "
  "terapêutica, assinale a afirmativa CORRETA.",
  "Revisões sistemáticas de ensaios clínicos randomizados de boa qualidade ocupam o topo da hierarquia de evidências terapêuticas.",
  [("Opiniões de especialistas ocupam o topo da hierarquia de evidências terapêuticas, por refletirem a prática clínica.",
    "Opinião de especialista é o nível mais baixo."),
   ("Relatos e séries de casos ocupam o topo da hierarquia de evidências terapêuticas, por descreverem pacientes reais.",
    "Séries de casos têm baixo nível de evidência."),
   ("Estudos de caso-controle ocupam o topo da hierarquia de evidências terapêuticas, por permitirem estudar desfechos raros.",
    "Úteis para desfechos raros, mas abaixo de ECR e revisões."),
   ("Estudos transversais ocupam o topo da hierarquia de evidências terapêuticas, por avaliarem grande número de pessoas.",
    "Transversais não estabelecem temporalidade.")],
  "Para terapêutica, o maior nível de evidência é a revisão sistemática (com ou sem metanálise) de ECR homogêneos e de boa qualidade.",
  "Oxford CEBM – níveis de evidência", "Confundir tamanho amostral ou experiência com nível de evidência.")

q(Q, D, "Avaliação pericial em doenças dermatológicas", "Dermatose ocupacional", 2, SIT, C,
  "Auxiliar de enfermagem desenvolve eczema nas mãos que melhora nas férias e piora ao retornar; suspeita-"
  "se de alergia à borracha das luvas. Considerando a investigação de dermatoses ocupacionais, assinale a "
  "afirmativa CORRETA.",
  "A suspeita de dermatite de contato alérgica é investigada pelo teste de contato, e a melhora nas férias reforça o nexo.",
  [("A suspeita de dermatite de contato alérgica é confirmada pela biópsia, sendo o teste de contato contraindicado em trabalhadores.",
    "O teste de contato (patch test) é o exame de escolha para a alérgica."),
   ("A suspeita de dermatite de contato irritativa é investigada pelo teste de contato, que é positivo na maioria desses casos.",
    "O teste de contato investiga sensibilização alérgica; na irritativa é negativo."),
   ("A melhora nas férias afasta relação com o trabalho, pois dermatoses ocupacionais persistem mesmo sem exposição.",
    "A melhora no afastamento sugere relação ocupacional."),
   ("A suspeita de dermatite de contato alérgica dispensa investigação, pois a profissão de saúde basta para o nexo.",
    "A profissão não basta; o nexo exige investigação.")],
  "Na dermatite de contato alérgica ocupacional, o teste de contato identifica o alérgeno; a melhora com o afastamento e a piora no retorno reforçam o nexo.",
  "Dermatoses ocupacionais – Ministério da Saúde", "Troca irritativa × alérgica.")

q(Q, D, "Avaliação pericial em doenças neurológicas", "Prognóstico funcional pós-AVC", 2, SIT, C,
  "Servidor de 52 anos teve AVC isquêmico há dois meses, com hemiparesia leve, marcha independente e "
  "afasia de expressão em melhora com fonoterapia. Exerce função administrativa. Considerando o "
  "prognóstico funcional, assinale a afirmativa CORRETA.",
  "A recuperação neurológica é mais intensa nos primeiros meses, justificando incapacidade temporária com reavaliação.",
  [("A recuperação neurológica se encerra nas primeiras semanas, justificando a conclusão definitiva de incapacidade permanente.",
    "A maior parte da recuperação ocorre nos primeiros 3–6 meses; é cedo para concluir."),
   ("A recuperação neurológica é irrelevante para a perícia, que deve concluir pela capacidade diante da marcha independente.",
    "A afasia repercute em função administrativa; o prognóstico é central."),
   ("A recuperação neurológica é imprevisível, impondo aposentadoria imediata a todo servidor com sequela de AVC.",
    "A conclusão depende da repercussão funcional e da evolução."),
   ("A recuperação neurológica depende apenas da extensão da lesão na imagem, dispensando a avaliação funcional atual.",
    "A avaliação funcional é indispensável.")],
  "Após AVC, a recuperação é mais acentuada nos primeiros 3 a 6 meses; em fase de reabilitação ativa, a conclusão adequada costuma ser incapacidade temporária com reavaliação, considerando a função exercida.",
  "Neurologia – prognóstico funcional pós-AVC", "Conclusões definitivas precoces.")

q(Q, D, "Avaliação pericial em doenças endócrinas e metabólicas", "Diabetes e atividade de risco", 2, SIT, C,
  "Motorista de ônibus com diabetes tipo 1 apresenta hipoglicemias graves recorrentes, com dois episódios "
  "de perda de consciência no último mês. Considerando a avaliação pericial da capacidade, assinale a "
  "afirmativa CORRETA.",
  "As hipoglicemias graves recorrentes geram incapacidade para a atividade de risco enquanto não houver controle.",
  [("O diagnóstico de diabetes tipo 1 gera, por si só, incapacidade permanente para qualquer atividade profissional.",
    "O diagnóstico não define incapacidade."),
   ("As hipoglicemias graves recorrentes são irrelevantes para a perícia quando a hemoglobina glicada está dentro da meta.",
    "Hipoglicemia com perda de consciência é risco à atividade, mesmo com HbA1c na meta."),
   ("As hipoglicemias graves recorrentes geram incapacidade apenas para atividades administrativas, não para a direção.",
    "O risco é maior justamente na direção profissional."),
   ("O diagnóstico de diabetes tipo 1 é incompatível com a habilitação profissional, impondo cassação definitiva da CNH.",
    "A aptidão é avaliada caso a caso.")],
  "Na perícia, o que define incapacidade é o risco e a repercussão funcional (hipoglicemias graves recorrentes) frente às exigências da atividade, sobretudo atividades de risco a si e a terceiros.",
  "Perícia médica – endocrinopatias e atividades de risco", "Diagnóstico como critério isolado.")

q(Q, D, "Classificação Internacional de Doenças (CID-10/CID-11)", "Estrutura da CID-10", 1, DIR, C,
  "Na emissão de laudos periciais, o correto uso da CID-10 é essencial. Considerando a estrutura dos "
  "capítulos da CID-10, assinale a afirmativa CORRETA.",
  "Os transtornos mentais e comportamentais são codificados no capítulo V, com códigos iniciados pela letra F.",
  [("Os transtornos mentais são codificados no capítulo VI, com códigos iniciados pela letra G.",
    "A letra G corresponde às doenças do sistema nervoso (capítulo VI)."),
   ("As doenças do sistema osteomuscular são codificadas no capítulo XIII, com códigos iniciados pela letra S.",
    "Osteomusculares usam a letra M; S/T são lesões e envenenamentos."),
   ("As doenças do aparelho circulatório são codificadas no capítulo IX, com códigos iniciados pela letra C.",
    "Circulatório usa a letra I; C corresponde a neoplasias malignas."),
   ("As doenças do aparelho respiratório são codificadas no capítulo X, com códigos iniciados pela letra R.",
    "Respiratório usa a letra J; R são sintomas e sinais.")],
  "CID-10: cap. V – F (transtornos mentais); VI – G (sistema nervoso); IX – I (circulatório); X – J (respiratório); XIII – M (osteomuscular); XIX – S/T (lesões).",
  "OMS – CID-10", "Letras vizinhas e confundíveis (F/G, M/S, I/C, J/R).")
