import matplotlib.pyplot as plt
import numpy as np
import time
import math

# Implementación de los algoritmos
def Mayoritario1(A, i, j):
    if i == j:
        return A[i]
    else:
        k  = math.ceil((i + j) // 2)
        m1 = Mayoritario1(A, i, k)
        m2 = Mayoritario1(A, k + 1, j)
        m  = None
        if m1 is not None:
            m = Comprobar(A, i, j, m1)
        if m2 is not None and m is None:
            m = Comprobar(A, i, j, m2)
        return m


def Comprobar(A, i, j, m):
    contador = 0
    #Compureba las ocurrencias de m (incluyendo A[j])
    for n in range(i, j + 1):
        if A[n] == m:
            contador += 1
    
    #Determina si es el elemento mayoritario o no
    if contador > (j - i + 1) // 2:
        return m
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
    #Numero de elementos
    n = j - i + 1
    
    #Caso base 1
    if n == 1:
        return A[i]
    
    #Caso base 2
    if n == 0:
        return

    #Crea C
    C = []
    k = i

    #Recorre toda la lista buscando pares
    while k < j:
        if A[k] == A[k+1]:
            C.append(A[k])
        k += 2
    
    #Si el tamaño es impar, se contempla el ultimo elemento como candidato
    if n % 2 == 1:
        C.append(A[j])
    
    return Candidato(C, 0, len(C) - 1)


"""""
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
"""""

def main():
    #Ejemplos para Mayoritario 1
    ejemplos = [
        [1,2,1,2,1,2,2],
        [1,6,6,3,6,6],
        [1,1,2,2,3,3,4,4],
        [8,5,3,1,2,6]
    ]

    #Muestra el ejemplo y el resultado de  
    for ejemplo in ejemplos:
        print("Ejemplo 1: ", ejemplo)
        r = Mayoritario1(ejemplo, 0, len(ejemplo) - 1)
        print("Resultado: ", r)
    
    # res = Mayoritario3(arr, 0, len(arr)-1)
    # print(res)

if __name__ == "__main__":
    main()