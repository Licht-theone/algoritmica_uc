# Implementación de los algoritmos
def Recursivo(A, hueco, ficha, m):
    if m >= len(A) - 2:
        Mostrar(A)
        return 0
    else:
        Mostrar(A)
        A[hueco], A[ficha] = A[ficha], A[hueco]
        n = len(A) // 2
        if ficha == n:
            m += 1
        if n - 1 <= ficha <= n + 1:
            m += 1
        if hueco - 1 <= ficha <= hueco + 1:
            return Recursivo(A, ficha, hueco - A[hueco], m) + 1
        elif A[hueco] == A[ficha + A[hueco]]:
            return Recursivo(A, ficha, ficha + A[hueco], m) + 1
        else:
            return Recursivo(A, ficha, ficha + A[hueco] * 2, m) + 1

def Mostrar(A):
    s = ''
    for i in range(len(A)):
        if A[i] == 1:
            s += '\33[42m  \33[0m  '
        elif A[i] == -1:
            s += '\33[43m  \33[0m  '
        else:
            s += '\33[47m  \33[0m  '
    print('\n' + s)

def Iterativo(A, tabl = False):
    return None

