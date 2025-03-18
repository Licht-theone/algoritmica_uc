import time
import matplotlib.pyplot as plt
import tracemalloc

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

def Iterativo(A, hueco, ficha, m):
    # Inicializacion de los datos que cambian(X')
    hueco_actual = hueco
    ficha_actual = ficha
    m_actual = m
    
    # Inicializa el stack
    stack = []

    n = len(A) // 2
    
    #Mostrar(A)  
    # Simula las llamadas recursivas hasta llegar al caso base (EsSencillo(X))
    while m_actual < len(A) - 2:  
        #Realiza el intercambio entre ficha y hueco
        A[hueco_actual], A[ficha_actual] = A[ficha_actual], A[hueco_actual]
        
        #Mostrar(A)
        
        #Se almacenan los datos que han cambiado en el stack
        stack.append((hueco_actual, ficha_actual, m_actual))
    
        # Se incrementa m en funcion de lo que ocurre en Recursivo
        nuevo_m = m_actual
        if ficha_actual == n:
            nuevo_m += 1
        if n - 1 <= ficha_actual <= n + 1:
            nuevo_m += 1
            
        # Calcula el siguiente estado
        if hueco_actual - 1 <= ficha_actual <= hueco_actual + 1:
            nuevo_hueco = ficha_actual
            nueva_ficha = hueco_actual - A[hueco_actual]
        elif A[hueco_actual] == A[ficha_actual + A[hueco_actual]]:
            nuevo_hueco = ficha_actual
            nueva_ficha = ficha_actual + A[hueco_actual]
        else:
            nuevo_hueco = ficha_actual
            nueva_ficha = ficha_actual + A[hueco_actual] * 2
        
        # Actualiza los datos
        hueco_actual = nuevo_hueco
        ficha_actual = nueva_ficha
        m_actual = nuevo_m
    
    Y = 0
    
    # Popea los elementos del stack para calcular Y
    while len(stack) > 0:
        hueco_actual, ficha_actual, m_actual = stack.pop()

        A[ficha_actual], A[hueco_actual] = A[hueco_actual], A[ficha_actual]
        
        A_copy = A.copy()
        A_copy.reverse()

        #Mostrar(A_copy)
        Y = Y + 1
    
    return Y * 2


val = Iterativo([-1, -1, 0, 1, 1], 2, 3, 0)
print()
print(val)


def main():
    ##Valores de prueba
    valores = [
        [-1, 0, 1],
        [-1, -1, 0, 1, 1],
        [-1, -1, -1, 0, 1, 1, 1],
        [-1 ,-1, -1, -1, 0, 1, 1, 1, 1],
        [-1, -1 ,-1, -1, -1, 0, 1, 1, 1, 1, 1]
    ]
    

    ## Casos de prueba
    Iterativo(valores[0], 1, 2, 0)
    print()

    Iterativo(valores[1], 2, 3, 0)
    print()
    
    Iterativo(valores[2], 3, 4, 0)
    print()
    
    Iterativo(valores[3], 4, 5, 0)
    print()
    
    Iterativo(valores[4], 5, 6, 0)

    # Medición de tiempos para n entre 10 y 1000 de 10 en 10
    tiempos = []
    valores_n = list(range(10, 1001, 10))

    print("[!] Calculando la evolucion del tiempo en funcion del numero de fichas")
    for n in valores_n:
        # Construir el tablero
        tablero = [-1] * n + [0] + [1] * n
        inicio = time.time()
        Iterativo(tablero.copy(), n, n + 1, 0)
        fin = time.time()
        tiempos.append(fin - inicio)

    with plt.style.context('ggplot'):
        plt.plot(valores_n, tiempos, label="Complejidad temporal")
        plt.title("Evolucion del tiempo en funcion del numero de fichas (n)")
        plt.xlabel("Numero de fichas")
        plt.ylabel("Tiempo (segundos)")
        plt.grid(True)
        plt.legend()
    
    plt.show()

    uso_memoria = []

    print("[!] Calculando la evolucion del uso de memoria en funcion del numero de fichas")
    for n in valores_n:
        tablero = [-1] * n + [0] + [1] * n
        tracemalloc.start()
        Iterativo(tablero.copy(), n, n + 1, 0)
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        uso_memoria.append(pico)
    
    with plt.style.context('ggplot'):
        plt.plot(valores_n, uso_memoria, label="Uso memoria")
        plt.title("Evolucion del uso de memoria en funcion del numero de fichas (n)")
        plt.xlabel("Numero de fichas")
        plt.ylabel("Tamaño en memoria (bytes)")
        plt.grid(True)
        plt.legend()
    plt.show()

if __name__ == "__main__":
    main() 