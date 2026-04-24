# Replace the "ANSWER HERE" for your answer

def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
    potencia = 1
    if exp == 0:
        return 1
    elif exp > 0:
        for b in range(exp):
            potencia *= base
    return potencia # Remove this line and implement


def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    sum_pows = 0
    for i in range(max_exp+1):
        sum_pows += power(base, i)
    return sum_pows  # Remove this line and implement
