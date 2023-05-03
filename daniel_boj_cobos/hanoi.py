""" Función para resolver el problema de las torres de Hanoi de forma
recursiva. """
def hanoi(discs, source_tower, destination_tower, auxiliar_tower):
    """ Para poder resolver el problema, hemos de tratar las torres como
    una pila, solo podemos retirar el disco superior, y manejar la torre
    a la que enviamos cada disco, ya que sea cual sea el número de discos,
    los movimientos siempre siguen la misma secuencia."""

    # Comenzamos por definir un caso base, cuando solo queda un disco en una torre.
    if discs == 1:
        # El movimiento final siempre será mover el disco de la torre origen a la torre destino.
        print(f"Mover el disco {discs} de la torre {source_tower} a la torre {destination_tower}")
        return

    # Si no es el caso base, debemos seguir dividiendo el problema a través de la recursividad.
    # El primer paso es mover todos los discos menos el último a la torre auxiliar.
    hanoi(discs-1, source_tower, auxiliar_tower, destination_tower)

    # Mostramos el movimiento que hemos realizado.
    print(f"Mover el disco {discs} de la torre {source_tower} a la torre {destination_tower}")

    # Por último, movemos los discos de la torre auxiliar a la torre de destino.
    hanoi(discs-1, auxiliar_tower, destination_tower, source_tower)

# Montamos el driver del programa.
if __name__ == "__main__":
    # Pedimos al usuario el número de discos.
    discos = int(input("Introduce el número de discos: "))

    # Llamamos a la función para resolver el problema.
    hanoi(discos, "A", "B", "C")

# Path: hanoi.py
