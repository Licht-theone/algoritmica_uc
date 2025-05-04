import math
import tracemalloc
import matplotlib.pyplot as plt

"""
Algoritmo voraz para la practica 4

Recibe como argumentos un vector con la lista de los valores de monedas (preferiblemente en orden ascendente)
y la cantidad a cambiar 
"""
def monedas_voraz(V, cantidad):
    V.sort(reverse=True) # Ordena de manera descendente

    MonedasSeleccionadas = [0] * len(V)
    cantidadRestante = cantidad

    while cantidadRestante > 0:
        i = 0
        # Busca una moneda adecuada a la cantidad restante
        for moneda in V:
            if moneda <= cantidadRestante:
                MonedasSeleccionadas[i] += 1
                cantidadRestante -= moneda
                break
            i += 1
    MonedasSeleccionadas.reverse() # Invertimos el resultado para asi que corresponda con el valor de las monedas       
    return MonedasSeleccionadas

"""
Algoritmo top-down para la practica 4

Recive como argumentos un vector con la lista de los valores de monedas y la cantidad a cambiar 
Calcula de manera recursiva una matriz con todas las posibles soluciones y despues la lista con el numero de monedas
para dar la solucion
"""
def monedas_topdown(valores, n):
    m = len(valores)
    A = [[-1 for _ in range(n + 1)] for _ in range(m)]
    
    monedas_usadas = [0] * m  # Lista para almacenar la cantidad de cada tipo de moneda
    
    # Calculamos el número mínimo de monedas usando el enfoque top-down
    monedas_topdown_rec(m - 1, n, valores, A)
    
    # Reconstruimos la solución
    reconstruir_solucion(m - 1, n, valores, A, monedas_usadas)
    
    return monedas_usadas

def monedas_topdown_rec(i, j, valores, A):
    # Casos bases
    if j == 0:
        return 0
    
    if i == 0:
        return j
    
    if A[i][j] != -1:
        return A[i][j]
    
    # Si el valor de la moneda actual es mayor que la cantidad a cambiar
    if valores[i] > j:
        resultado = monedas_topdown_rec(i - 1, j, valores, A)
    else:
        # Decidimos si usar la moneda actual o no
        no_usar = monedas_topdown_rec(i - 1, j, valores, A)
        usar = 1 + monedas_topdown_rec(i, j - valores[i], valores, A)
        resultado = min(no_usar, usar)
    
    # Guardamos el resultado en la Aización
    A[i][j] = resultado
    return resultado

def reconstruir_solucion(i, j, valores, A, monedas_usadas):
    if j == 0:
        return
    
    if i == 0:
        # Si solo podemos usar la moneda más pequeña
        monedas_usadas[i] = j
        return
    
    # Si no usamos la moneda actual
    if valores[i] > j or A[i][j] == A[i - 1][j]:
        reconstruir_solucion(i - 1, j, valores, A, monedas_usadas)
    else:
        # Usamos una moneda del valor actual
        monedas_usadas[i] += 1
        reconstruir_solucion(i, j - valores[i], valores, A, monedas_usadas)

"""
Algoritmo bottom-up para la practica 4

Recive como argumentos un vector con la lista de los valores de monedas y la cantidad a cambiar
"""
def monedas_bottomup(valores, n):
    m = len(valores)
    # Creamos una tabla A con (m+1) filas y (n+1) columnas.
    # A[i][j] contendrá el mínimo número de monedas necesarias para cambiar j usando las primeras i monedas.
    A = [[math.inf] * (n + 1) for _ in range(m + 1)]
    
    # Inicializamos la matriz
    for i in range(m + 1):
        A[i][0] = 0
    
    # Rellenamos la tabla A 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if valores[i-1] > j:
                A[i][j] = A[i-1][j]
            else:
                A[i][j] = min(A[i-1][j], A[i][j - valores[i-1]] + 1)
    
    # Si no es posible lograr la cantidad, la solución sigue siendo infinito.
    if A[m][n] == math.inf:
        return None

    # Comprobamos la solucion
    counts = [0] * m
    i = m
    j = n
    while j > 0 and i > 1:
        # Si el valor mínimo para j usando las primeras i monedas es el mismo
        # que usando las primeras (i-1), en la solución no se ha utilizado la moneda valores[i-1].
        if A[i][j] == A[i-1][j]:
            i -= 1
        else:
            # En otro caso, se ha utilizado la moneda valores[i-1]
            counts[i-1] += 1
            j -= valores[i-1]
    # En caso de que solo quede la moneda de menor valor (valores[0]), se cubre el resto.
    if j > 0:
        counts[0] += j

    return counts


def medir_memoria_topdown_tracemalloc(monedas, n):
    """
    Simula la creación de la tabla DP para el algoritmo top-down.
    La tabla se crea con dimensiones: m x (n+1),
    donde m es el número de tipos de monedas.
    
    Se inicia tracemalloc y, tras crear la tabla, se obtiene
    el pico de memoria asignada durante la ejecución.
    """
    m = len(monedas)
    tracemalloc.start()
    tabla_td = [[-1 for _ in range(n + 1)] for _ in range(m)]
    # Obtenemos la memoria actual y el pico asignado
    mem_actual, pico_memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return pico_memoria

def medir_memoria_bottomup_tracemalloc(monedas, n):
    """
    Simula la creación de la tabla DP para el algoritmo bottom-up.
    La tabla se crea con dimensiones: (m + 1) x (n+1),
    donde m es el número de tipos de monedas.
    
    Se inicia tracemalloc y, tras crear la tabla, se obtiene
    el pico de memoria asignada durante la ejecución.
    """
    m = len(monedas)
    tracemalloc.start()
    tabla_bu = [[math.inf] * (n + 1) for _ in range(m + 1)]
    # Obtenemos la memoria actual y el pico asignado
    mem_actual, pico_memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return pico_memoria

def main():

    Monedas = [1, 2, 5, 10]
    print("Algoritmo voraz: lista:", Monedas, ". Cantidad: 16")
    A = monedas_voraz(Monedas, 16)
    print(A)

    Monedas = [1, 2, 5, 10]
    print("Algoritmo top_down: lista:", Monedas, ". Cantidad: 16")
    A = monedas_topdown(Monedas, 16)
    print(A)

    Monedas = [1, 2, 5, 10]
    print("Algoritmo top_down: lista:", Monedas, ". Cantidad: 16")
    A = monedas_bottomup(Monedas, 16)
    print(A)


    # CREACION DE LAS GRAFICAS PARA EL APARTADO 2 Y 3 #
    print("Creando grafica de los recursos de memoria para el algoritmo top-down")

    monedas_euro   = [1, 2, 5, 10]           
    monedas_ingles = [1, 3, 6, 12, 24, 30]     

    # Rango de cantidades a cambiar (n): de 10 a 1000, de 10 en 10.
    valores_n = list(range(10, 1001, 10))

    memoria_topdown_euro    = []
    memoria_bottomup_euro   = []
    memoria_topdown_ingles  = []
    memoria_bottomup_ingles = []

    # Medición de memoria para cada valor de n
    for n in valores_n:
        memoria_topdown_euro.append(medir_memoria_topdown_tracemalloc(monedas_euro, n))
        memoria_bottomup_euro.append(medir_memoria_bottomup_tracemalloc(monedas_euro, n))
        memoria_topdown_ingles.append(medir_memoria_topdown_tracemalloc(monedas_ingles, n))
        memoria_bottomup_ingles.append(medir_memoria_bottomup_tracemalloc(monedas_ingles, n))

    # Graficamos los resultados
    plt.figure(figsize=(12, 6))

    # Subgráfica para el sistema del euro
    plt.subplot(1, 2, 1)
    plt.plot(valores_n, memoria_topdown_euro, marker='o', label='Top-Down')
    plt.plot(valores_n, memoria_bottomup_euro, marker='s', label='Bottom-Up')
    plt.title('Uso de memoria (Sistema Euro)')
    plt.xlabel('Cantidad a cambiar (n)')
    plt.ylabel('Memoria (bytes)')
    plt.legend()

    # Subgráfica para el sistema inglés
    plt.subplot(1, 2, 2)
    plt.plot(valores_n, memoria_topdown_ingles, marker='o', label='Top-Down')
    plt.plot(valores_n, memoria_bottomup_ingles, marker='s', label='Bottom-Up')
    plt.title('Uso de memoria (Sistema Inglés)')
    plt.xlabel('Cantidad a cambiar (n)')
    plt.ylabel('Memoria (bytes)')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()