import click
from muebleria.mueble import Silla, Mesa, Armario
from muebleria.main import main

@click.group()
def cli():
    """Interfaz de Línea de Comandos para la Mueblería"""
    pass

@cli.command()
def mostrar():
    """Muestra los muebles en inventario"""
    main()

@cli.command()
@click.option("--tipo", type=click.Choice(["silla", "mesa", "armario"]), help="Tipo de mueble a agregar")
@click.option("--material", prompt="Material", help="Material del mueble")
@click.option("--precio", type=float, prompt="Precio", help="Precio del mueble")
@click.option("--extra", prompt="Extra", help="Respaldo (Silla), Forma (Mesa), Nº puertas (Armario)")
def agregar(tipo, material, precio, extra):
    """Agrega un mueble al inventario"""
    if tipo == "silla":
        mueble = Silla(material, precio, extra)
    elif tipo == "mesa":
        mueble = Mesa(material, precio, extra)
    elif tipo == "armario":
        mueble = Armario(material, precio, int(extra))
    
    with open("muebles.json", "a") as f:
        f.write(str(mueble.__dict__) + "\n")

    print(f"{tipo.capitalize()} agregado correctamente.")

if __name__ == "__main__":
    cli()
