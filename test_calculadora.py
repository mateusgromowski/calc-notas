import pytest

from calculadora import calcula_media, situacao, situacao_final

def test_media_simples():
    n1, n2, n3 = 7.0, 8.0, 9.0

    resultado = calcula_media(n1, n2, n3)

    assert resultado == 8.25

def test_aluno_aprovado():
    assert situacao(7.0) == "aprovado"
    assert situacao(8.5) == "aprovado"
    assert situacao(10.0) == "aprovado"

def test_aluno_recuperacao():
    assert situacao(4.0) == "recuperacao"
    assert situacao(6.9) == "recuperacao"

def test_aluno_reprovado():
    assert situacao(3.9) == "reprovado"
    assert situacao(0.0) == "reprovado"

def test_nota_acima_de_10_eh_invalida():
    with pytest.raises(ValueError):
        calcula_media(11.0, 7.0, 8.0)

def test_nota_negativa_eh_invalida():
    with pytest.raises(ValueError):
        calcula_media(7.0, -1.0, 8.0)

def test_aluno_aprovado_na_recuperacao():
    assert situacao_final(6.0, 6.0) == "aprovado na recuperacao"
    assert situacao_final(6.9, 8.0) == "aprovado na recuperacao"

def test_aluno_reprovado_na_recuperacao():
    assert situacao_final(4.0, 4.0) == "reprovado na recuperacao"

def test_notas_invalidas_situacao_final():
    with pytest.raises(ValueError):
        situacao_final(11.0, 5.0)

    with pytest.raises(ValueError):
        situacao_final(5.0, -1.0)

# Esse trabalho foi muito legal
# pois me fez lembrar de uma frase do autor do livro "Learn To Program", Chris Pine: 
# "Programming is not about what you know it's about what you can figure out"