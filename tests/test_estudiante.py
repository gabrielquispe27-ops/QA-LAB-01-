from src.estudiante import aprobado


def test_aprobado_nota_mayor_a_11():
    """Test que verifica si nota > 11 es aprobado"""
    assert aprobado(12) == True


def test_aprobado_nota_igual_a_11():
    """Test que verifica si nota = 11 es aprobado"""
    assert aprobado(11) == True


def test_desaprobado_nota_menor_a_11():
    """Test que verifica si nota < 11 es desaprobado"""
    assert aprobado(10) == False


def test_desaprobado_nota_cero():
    """Test que verifica si nota = 0 es desaprobado"""
    assert aprobado(0) == False


def test_aprobado_nota_maxima():
    """Test que verifica si nota máxima (20) es aprobado"""
    assert aprobado(20) == True
