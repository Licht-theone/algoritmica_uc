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

def main():
    
    Monedas = [1, 2, 5, 10, 20, 50]

    A = monedas_voraz(Monedas, 103)

    print(A)

if __name__ == "__main__":
    main()