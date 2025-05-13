def laberinto_numerico(T):
    n = len(T)
    # Inicializar matriz solución con ceros
    S = [[0 for _ in range(n)] for _ in range(n)]
    
    # Llamar a la función recursiva empezando en (0,0)
    if RLaberinto_numerico(T, S, 0, 0, 1):
        return S
    else:
        return None

def RLaberinto_numerico(T, S, i, j, p):
    n = len(T)
    
    #Casos base:

    # Si estamos fuera del tablero
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    
    # Si ya hemos visitado esta casilla
    if S[i][j] != 0:
        return False
    
    # Si estamos en la posición final 
    if i == n-1 and j == n-1:
        S[i][j] = p
        return True
    
    S[i][j] = p
    d = T[i][j] #Distancia a recorrer
    
    # Probar los cuatro movimientos posibles 
    
    # Mover hacia abajo 
    if RLaberinto_numerico(T, S, i + d, j, p + 1):
        return True
    
    # Mover hacia arriba 
    if RLaberinto_numerico(T, S, i - d, j, p + 1):
        return True
    

    # Mover a la derecha
    if RLaberinto_numerico(T, S, i, j + d, p + 1):
        return True
    
    # Mover a la izquierda
    if RLaberinto_numerico(T, S, i, j - d, p + 1):
        return True
    

    # Si ningún movimiento funciona, desahemos los cambios hechos
    S[i][j] = 0
    return False

def main():
    # Ejemplo del enunciado
    T = [
        [2, 3, 3, 2],
        [2, 1, 1, 1],
        [3, 2, 2, 2],
        [2, 2, 2, 0]
    ]
    
    solucion = laberinto_numerico(T)
    
    if solucion:
        print("Solución encontrada:")
        for fila in solucion:
            print(fila)
    else:
        print("No hay solución para este laberinto.")

if __name__ == "__main__":
    main()