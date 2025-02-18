import time
import matplotlib.pyplot as plt
import numpy as np

def suma_dist(arr):
    n = len(arr)
    suma_distancia = 0
    
    for i in range(n):
        encontrado = False
        num = arr[i]
        dist = 0
        
        # busca el primer numero a la derecha que sea mayor
        for j in range(i + 1, n):
            dist += 1
            if arr[j] > num:
                encontrado = True
                break

        # si no se encuentra un numero mayor, se determina que existe otro mayor al final de la lista
        if not encontrado:
            dist += 1

        #suma la distancia
        suma_distancia += dist 
    
    return suma_distancia

def medir_tiempos_mejor_caso():

    # Mide los tiempos de ejecución de sumadist en el mejor caso.
    
    entradas = list(range(10_000, 1_000_001, 10_000))
    tiempos = []
    for entrada in entradas:
        arr = list(range(1, entrada + 1))  # Secuencia creciente
        inicio = time.time()
        suma_dist(arr)
        fin = time.time()
        tiempos.append(fin - inicio)
    return entradas, tiempos

def medir_tiempos_peor_caso():
    
    # Mide los tiempos de ejecución de sumadist en el peor caso.

    entradas = list(range(1_000, 10_001, 1_000))
    tiempos = []
    for entrada in entradas:
        arr = list(range(entrada, 0, -1))  # Secuencia decreciente
        inicio = time.time()
        suma_dist(arr)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return entradas, tiempos

# Main del programa

def main():
    
    # Listas para probar el algoritmo
    ejemplos = [
    [1, 2, 3, 4],
    [5, 4, 3, 2, 1],
    [5, 4, 3, 4, 1],
    [1, 1, 1, 1] 
    ]

    for i in range(4) : 
        t = time.time()
        print(suma_dist(ejemplos[i]))
        T = time.time() - t
        print("Tiempo de ejecucion: " + str(T) + "s")

    # Graficamos el mejor caso
    entradas_mejor, tiempos_mejor = medir_tiempos_mejor_caso()

    #TODO Fix graficas
    with plt.style.context('ggplot'):
        plt.plot(entradas_mejor, tiempos_mejor, label="Mejor caso (secuencia creciente)")
        plt.title("Tiempos de ejecución en el mejor caso")
        plt.xlabel("Tamaño n del array")
        plt.ylabel("Tiempo (segundos)")
        plt.grid(True)
        plt.legend()
    
    plt.show()
    

    

# Ejecuta la funcion main en el caso de que se ejecute como un programa principal
if __name__ == "__main__":
    main()
