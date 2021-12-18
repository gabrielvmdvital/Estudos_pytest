import pytest

def soma (x, y):
    return float(x) + float(y)


def test_soma_1():
    assert soma(10, 20) == 30

def test_soma_2():
    assert soma('10', '20.5') == 30.5


def test_soma_3():
    with pytest.raises(ValueError):
        soma("Ola", "mundo")
