import matplotlib.pyplot as plt
import numpy as np
import time

# Implementación de los algoritmos
def Mayoritario1(A, i, j):
    if i == j:
        return A[i]
    else:
        k  = (i + j) // 2
        m1 = Mayoritario1(A, i, k)
        m2 = Mayoritario1(A, k + 1, j)
        m  = None
        if m1 is not None:
            m = Comprobar(A, i, j, m1)
        if m2 is not None and m is None:
            m = Comprobar(A, i, j, m2)
        return m

def Comprobar(A, i, j, m):
    return None

def Mayoritario2(A, i, j):
    D = {}
    for k in range(i, j + 1):
        if A[k] not in D:
            D.update({A[k] : 1})
        else:
            D[A[k]] = D[A[k]] + 1
    for key, val in D.items():
        if val > (j - i + 1) // 2:
            return key
    return None

def Mayoritario3(A, i, j):
    B = []
    for k in range(i, j + 1):
        B.append(A[k])
    m = Candidato(B, i, j)
    if m is not None:
        m = Comprobar(A, i, j, m)
    return m

def Candidato(A, i, j):
    return None

# Ejemplos de entrada

# Complejidad temporal
n = 1000001
T = [[0], [0], [0]]
A = [i for i in range(n)]

for i in range(n // 100, n, n // 100):
    t = time.time()
    Mayoritario1(A, 0, i)
    T[0].append(time.time() - t)

    t = time.time()
    Mayoritario2(A, 0, i)
    T[1].append(time.time() - t)

    t = time.time()
    Mayoritario3(A, 0, i)
    T[2].append(time.time() - t)

    print(f'Iteración {i // 10000} de 100')
