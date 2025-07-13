import pytest
from unitest.unitest import calcular_cubo, calcular_paralelogramo, calcular_piramide
from utils.utils import ler_csv

def test_calcular_cubo():
    aresta = 5
    resultado_esperado = 150

    resultado_obtido = calcular_cubo(aresta)

    assert resultado_esperado == resultado_obtido

def test_negativo_calcular_cubo():
    aresta = -5
    with pytest.raises(ValueError, match="A aresta precisa ser um numero positivo."):
        calcular_cubo(aresta)


def test_calcular_paralelogramo():
    base = 10
    altura = 4
    resultado_esperado = 40

    resultado_obtido = calcular_paralelogramo(base, altura)

    assert resultado_esperado == resultado_obtido


def test_calcular_piramide():
    base = 6
    apotema = 8
    resultado_esperado = 132

    resultado_obtido = calcular_piramide(base, apotema)

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('base, apotema, resultado_esperado, tipo',
                         ler_csv('./fixtures/massa_piramide.csv')
                         )
def test_calcular_piramide_csv(base, apotema, resultado_esperado, tipo):
    if tipo == 'positivo':
        resultado_obtido = calcular_piramide(int(base), int(apotema))
        assert int(resultado_esperado) == resultado_obtido
    else:
        with pytest.raises(ValueError, match="A base e a apotema precisa ser um numero positivo."):
            calcular_piramide(int(base),int(apotema))