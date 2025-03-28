# clases relacionadas con los muebles
from abc import ABC, abstractmethod

class Mueble(ABC):
    """Clase base para todos los muebles"""
    
    def __init__(self, material: str, precio: float):
        self.material = material
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """Método abstracto para calcular el precio final"""
        pass

    def aplicar_descuento(self, porcentaje: float):
        """Aplica un descuento al precio del mueble"""
        self.precio -= self.precio * (porcentaje / 100)

class Silla(Mueble):
    def __init__(self, material: str, precio: float, respaldo: str):
        super().__init__(material, precio)
        self.respaldo = respaldo

    def calcular_precio_final(self) -> float:
        return self.precio * 1.10  # 10% extra por ensamblaje

class Mesa(Mueble):
    def __init__(self, material: str, precio: float, forma: str):
        super().__init__(material, precio)
        self.forma = forma

    def calcular_precio_final(self) -> float:
        return self.precio * 1.15  # 15% extra por tamaño

class Armario(Mueble):
    def __init__(self, material: str, precio: float, puertas: int):
        super().__init__(material, precio)
        self.puertas = puertas

    def calcular_precio_final(self) -> float:
        return self.precio + (self.puertas * 50)  # 50 extra por puerta
