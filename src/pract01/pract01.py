import time

def suma_dist(arr):
    n = len(arr)
    suma_distancia = 0
    
    for i in range(n):
        num = arr[i]
        dist = 0
        
        # busca el primer numero a la derecha que sea mayor
        for j in range(i + 1, n):
            dist += 1
            if arr[j] > num:
                break
        else:
            # si no se encuentra un numero mayor, se determina que existe otro mayor al final de la lista
            dist += 1

        #suma la distancia
        suma_distancia += dist 
    
    return suma_distancia

# Main del programa
def main():
    # Listas para probar el algoritmo
    arr1 = [1] * 10000
    arr2 = [6,2,3,4,5]
    
    ## EJEMPLO DE USAR TIME ##
    t = time.time()
    print(suma_dist(arr2))
    T = time.time() - t
    print("Tiempo de ejecucion: " + str(T) + "s")

# Ejecuta la funcion main en el caso de que se ejecute como un programa principal
if __name__ == "__main__":
    main()
