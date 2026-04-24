# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lst_new = []
    for lista in matrix:
        for element in lista:
            lst_new.append(element)
    return lst_new


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    sum_lst = []
    for lista in matrix:
        sum = 0
        for element in lista:
            sum += element
        sum_lst.append(sum)
    return sum_lst  # Remove this line and implement


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    sum_col = matrix[0]
    for i in range (1, len(matrix)):
        for j in range( len(matrix[i]) ):
            sum_col[j] += matrix[i][j]
    return sum_col
