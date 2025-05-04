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
        ## Busca una moneda adecuada a la cantidad restante
        for moneda in V:
            if moneda <= cantidadRestante:
                MonedasSeleccionadas[i] += 1
                cantidadRestante -= moneda
                break
            i += 1
    MonedasSeleccionadas.reverse() ## Invertimos el resultado para asi que corresponda con el valor de las monedas       
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
    A = monedas_topdown(Monedas, 16)
    print(A)

if __name__ == "__main__":
    main()