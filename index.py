# Definición del tablero según la imagen (0 representa una casilla vacía)
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def es_valido(tab, num, pos):
    # Verificar fila
    for j in range(9):
        if tab[pos[0]][j] == num and pos[1] != j:
            return False

    # Verificar columna
    for i in range(9):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False

    # Verificar subcuadrícula de 3x3
    caja_x = pos[1] // 3
    caja_y = pos[0] // 3

    for i in range(caja_y * 3, caja_y * 3 + 3):
        for j in range(caja_x * 3, caja_x * 3 + 3):
            if tab[i][j] == num and (i, j) != pos:
                return False

    return True

def encontrar_vacio(tab):
    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                return (i, j)  # fila, columna
    return None

def resolver_sudoku(tab):
    vacio = encontrar_vacio(tab)
    if not vacio:
        return True  # Sudoku resuelto
    else:
        fila, col = vacio

    for num in range(1, 10):
        if es_valido(tab, num, (fila, col)):
            tab[fila][col] = num

            if resolver_sudoku(tab):
                return True

            tab[fila][col] = 0  # Revertir intento (backtrack)

    return False

def imprimir_tablero(tab):
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")

print("--- TABLERO ORIGINAL ---")
imprimir_tablero(tablero)

if resolver_sudoku(tablero):
    print("\n--- SOLUCIÓN ENCONTRADA ---")
    imprimir_tablero(tablero)
else:
    print("\nNo existe solución para este Sudoku.")