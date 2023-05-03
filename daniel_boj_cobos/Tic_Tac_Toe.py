"""El juego del gato o tres en raya es un juego para dos jugadores (X y O)"""
from random import randrange

def display_board(board):
    """La función acepta un parámetro el cual contiene el estado actual del tablero
    y lo muestra en la consola."""
    print (
        f"""
        +-------+-------+-------+
        |       |       |       |
        |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
        |       |       |       |
        +-------+-------+-------+
        """)


def enter_move(board):
    """La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    verifica la entrada y actualiza el tablero acorde a la decisión del usuario."""

    while True:
        square_num = int(input("Inserta tu movimiento: "))

        if square_num not in range(1, 10):
            print("La casilla escogida no es válida, por favor, inténtalo de nuevo.")
            continue

        for i in range(3):
            for j in range (3):
                if square_num == board[i][j]:
                    board[i][j] = "0"
                    return

        print("La casilla escogida no es válida, por favor, inténtalo de nuevo.")


def make_list_of_free_fields(board):
    """La función examina el tablero y construye una lista de todos los cuadros vacíos.
    La lista esta compuesta por tuplas, cada tupla es un par de números que indican
    la fila y columna."""

    free_squares = []

    for i in range(3):
        for j in range(3):
            if board[i][j] != '0' and board[i][j] != 'X':
                free_squares.append(tuple([i, j]))

    return free_squares

def victory_for(board, sign):
    """La función analiza el estatus del tablero para verificar si
    el jugador que utiliza las 'O's o las 'X's ha ganado el juego."""

    wining_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], \
                           [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    squares = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), \
               6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

    for comb in wining_combinations:
        if all(board[squares[square][0]][squares[square][1]] == sign for square in comb):
            return True

    return False

def draw_move(board):
    """La función dibuja el movimiento de la máquina y actualiza el tablero."""


    while True:
        computer_square = randrange(1, 10)

        for i in range(3):
            for j in range(3):
                if board[i][j] == computer_square:
                    board[i][j] = "X"
                    return

def main():
    """La función ejecuta el programa completo."""
    board = [
        [1, 2, 3],
        [4, "X", 6],
        [7, 8, 9]
        ]

    for i in range(4):
        display_board(board)
        enter_move(board)
        display_board(board)
        draw_move(board)

        if victory_for(board, "X"):
            display_board(board)
            print("Has perdido!")
            break

        if victory_for(board, "0"):
            display_board(board)
            print("Has ganado!")
            break

    if not victory_for(board, "0") and not victory_for(board, "X"):
        display_board(board)
        print("Es un empate!")

main()
