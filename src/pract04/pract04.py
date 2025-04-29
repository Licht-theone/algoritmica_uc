"""
Algoritmo voraz para la practica 4

Recive como argumentos un vector con la lista de los valores de monedas (preferiblemente en orden ascendente)
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

def monedas_topdown(V, cantidad):
    m = len(V)
    M = [ [ None ] * (m) for _ in range(cantidad+1) ]
    return rec_monedas_topdown(cantidad, len(V), M, V)

def rec_monedas_topdown(j, i, M, V):
    ## Casos base
    if j == 0:
        return 0

    if i == 1:
        return j 

    if M[j][i] != None:
        return M[j][i]

    if V[i] > j:
        M[j][i] = rec_monedas_topdown(j, i-1, M, V)
    else:
        M[j][i] = min(rec_monedas_topdown(j, i-1, M, V), 1 + rec_monedas_topdown(j - V[i], i, M, V))

    return M[j][i]

def main():

    Monedas = [1, 2, 5, 10, 20, 50]
    print("Algoritmo voraz: lista:", Monedas, ". Cantidad: 103")
    A = monedas_voraz(Monedas, 103)
    print(A)

    A = monedas_topdown(Monedas, 103)
    print(A)

if __name__ == "__main__":
    main()