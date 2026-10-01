"""Helper para escrever questões-fonte.

Cada questão é escrita com a alternativa correta separada das erradas;
o script de build sorteia as letras de forma balanceada (A–E ~20% cada).
"""

def q(lista, disciplina, tema, subtema, dif, tipo, comando, enunciado,
      correta, erradas, comentario, fundamento, pegadinha,
      verificar=False, texto=None):
    assert len(erradas) == 4, enunciado[:60]
    for e in erradas:
        assert isinstance(e, tuple) and len(e) == 2, enunciado[:60]
    lista.append(dict(
        disciplina=disciplina, tema=tema, subtema=subtema, dificuldade=dif,
        tipo_enunciado=tipo, comando=comando, enunciado=enunciado,
        correta=correta, erradas=erradas, comentario_correta=comentario,
        fundamento=fundamento, pegadinha=pegadinha, verificar=verificar,
        texto=texto,
    ))
