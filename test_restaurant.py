import pytest
from restaurant import Restaurant


# Para a execução dos testes assim que encontra uma falha:
# > pytest test_restaurant -x

def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero():
    restaurante = Restaurant("Pizzaria X")
    assert restaurante.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero():
    restaurante = Restaurant("Pizzaria X", 1)
    assert restaurante.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurant("Pizzaria X", -1)


def test_adiciona_um_pedido_na_fila():
    restaurante = Restaurant("Pizzaria X", 1)
    restaurante.adiciona_pedido()
    assert restaurante.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila():
    restaurante = Restaurant("Pizzaria X", 1)
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == 0


def test_remove_um_pedido_na_fila_vazia():
    restaurante = Restaurant("Pizzaria X")
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == 0
