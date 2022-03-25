import sys
sys.path.append('C:/Users/erick/proyectos/git/prueba_2')

from src.calc import get_fractions

# 1) Malas practicas
def test_get_fractions():
  assert get_fractions("10") == 10

def test_get_fractions_2():
  assert get_fractions("7/4") == 1.75

def test_get_fractions_3():
  assert get_fractions("-1") == -1


# 2) Buenas practicas
import pytest

def obtener_datos_test_get_fractions():
        return [(10,10), ("7/4",1.75), (-1,-1)]

@pytest.mark.parametrize('num1, esperado', obtener_datos_test_get_fractions())
def test_get_fractions_parametrize(num1, esperado):
        assert get_fractions(num1) == esperado

# 3) Marks
#   skip
@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_convertir_binario():
    ...

#   xfail
@pytest.mark.xfail
def test_get_fractions_falla():
    assert get_fractions("diez") == "diez"

#   Escribir una marca personal
@pytest.mark.mi_marca
def test_get_fractions_mi_marca():
    assert get_fractions("2/4") == 0.5