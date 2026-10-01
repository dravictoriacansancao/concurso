"""Taxonomia do edital (Anexo II) – Médico Perito Clínico Geral, Porto Calvo/AL 2026."""

DISCIPLINAS = {
    # nome: (nº questões, peso, taxa de acerto inicial estimada)
    "Português":      (10, 1.1, 0.60),
    "Constitucional": (5,  1.1, 0.45),
    "Informática":    (5,  1.1, 0.50),
    "Perícia":        (15, 2.6, 0.80),
    "SUS":            (15, 2.6, 0.55),
}

TEMAS = {
    "Português": [
        "Fonologia", "Interpretação e Análise Textual", "Morfologia",
        "Redação Oficial", "Semântica", "Sintaxe"],
    "Constitucional": [
        "Administração Pública na CF", "Aplicabilidade e interpretação das normas",
        "Controle de constitucionalidade", "Direitos e garantias fundamentais",
        "Direitos políticos", "Federalismo e organização do Estado",
        "Organização dos Poderes", "Poder constituinte", "Princípios fundamentais",
        "Processo legislativo", "Remédios constitucionais", "Responsabilidade do Estado",
        "Segurança pública na Constituição", "Sistema tributário nacional",
        "Supremacia da Constituição"],
    "Informática": [
        "Aplicativos de escritório", "Conceitos básicos de hardware e software",
        "Conceitos de internet, intranet e redes", "Conceitos de segurança da informação e proteção de dados",
        "Conceitos de sistemas operacionais", "Conceitos sobre armazenamento e gerenciamento de arquivos",
        "Conceitos sobre navegadores e ferramentas de busca", "Conceitos sobre protocolos de comunicação na internet",
        "Conceitos sobre redes sociais e ferramentas colaborativas", "E-mail e comunicação eletrônica no ambiente corporativo",
        "Ferramentas de backup e recuperação de dados", "Noções de computação em nuvem",
        "Utilização de planilhas eletrônicas"],
    "Perícia": [
        "Avaliação da capacidade laborativa", "Avaliação de dano corporal e nexo causal",
        "Avaliação de invalidez e incapacidade permanente",
        "Avaliação pericial em doenças cardiovasculares", "Avaliação pericial em doenças dermatológicas",
        "Avaliação pericial em doenças endócrinas e metabólicas", "Avaliação pericial em doenças infecciosas",
        "Avaliação pericial em doenças neurológicas", "Avaliação pericial em doenças osteomusculares",
        "Avaliação pericial em doenças psiquiátricas", "Avaliação pericial em doenças respiratórias",
        "Bioética aplicada à perícia médica", "Classificação Internacional de Doenças (CID-10/CID-11)",
        "Diagnóstico diferencial em clínica médica", "Doenças crônicas incapacitantes",
        "Doenças ocupacionais e relacionadas ao trabalho", "Epidemiologia clínica aplicada à perícia",
        "Exame clínico direcionado à perícia médica", "Incapacidade temporária / permanente",
        "Interpretação de exames complementares", "Medicina baseada em evidências",
        "Nexo técnico epidemiológico", "Perícia médica previdenciária",
        "Prognóstico funcional das principais doenças", "Semiologia médica aplicada à perícia"],
    "SUS": [
        "APS e ESF", "CF/88 arts. 196 a 200", "Controle social", "Financiamento",
        "Gestão municipal do SUS", "Indicadores e monitoramento",
        "Lei nº 8.080/1990", "Lei nº 8.142/1990"],
}
