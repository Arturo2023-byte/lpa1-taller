# ejecutar el programa y probar las clases

from rich.console import Console
from rich.table import Table
from mueble import Silla, Mesa, Armario

console = Console()

def main():
    muebles = [
        Silla("Madera", 150, "Alto"),
        Mesa("Metal", 300, "Redonda"),
        Armario("Madera", 500, 3)
    ]

    table = Table(title="Inventario de Muebles")
    table.add_column("Tipo", style="cyan")
    table.add_column("Material", style="green")
    table.add_column("Precio ($)", style="yellow")
    
    for mueble in muebles:
        table.add_row(mueble.__class__.__name__, mueble.material, str(mueble.calcular_precio_final()))

    console.print(table)

if __name__ == "__main__":
    main()

