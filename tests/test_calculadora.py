from src.Calculadora import suma, resta

def test_suma():
    assert suma(3, 2) == 5

def test_resta():
    assert resta(10, 4) == 6

