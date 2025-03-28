# pruebas unitarias utilizando pytest
import pytest
from muebleria.mueble import Silla, Mesa, Armario

def test_precio_final():
    silla = Silla("Madera", 100, "Bajo")
    mesa = Mesa("Metal", 200, "Cuadrada")
    armario = Armario("Madera", 400, 2)

    assert silla.calcular_precio_final() == pytest.approx(110.0)
    assert mesa.calcular_precio_final() == pytest.approx(230.0)
    assert armario.calcular_precio_final() == pytest.approx(500.0)

