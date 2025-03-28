# Objetivo: Permitir agregar y listar muebles en un inventario.
class Inventario:
    def __init__(self):
        self.muebles = []

    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)

    def mostrar_muebles(self):
        for mueble in self.muebles:
            print(f"{mueble.__class__.__name__}: {vars(mueble)}")

import json

def guardar_muebles(muebles, archivo="muebles.json"):
    with open(archivo, "w") as f:
        json.dump([mueble.__dict__ for mueble in muebles], f, indent=4)

def cargar_muebles(archivo="muebles.json"):
    with open(archivo, "r") as f:
        datos = json.load(f)
        return [Mueble(**mueble) for mueble in datos]
    
def cargar_muebles(archivo="muebles.json"):
    with open(archivo, "r") as f:
        datos = json.load(f)
        muebles = []
        for item in datos:
            if item["tipo"] == "Silla":
                mueble = Silla(item["material"], item["precio"], item["respaldo"])
            elif item["tipo"] == "Mesa":
                mueble = Mesa(item["material"], item["precio"], item["forma"])
            elif item["tipo"] == "Armario":
                mueble = Armario(item["material"], item["precio"], item["puertas"])
            muebles.append(mueble)
        return muebles
