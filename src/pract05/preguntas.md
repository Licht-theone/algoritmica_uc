## PREGUNTA 1 ##

laberinto_numerico(T[1..n, 1..n]):
    S[1..n, 1..n] <- (0,..,0),(0,..0)
    if RLaberinto_numerico(T[1..n, 1..n], S[1..n, 1..n], 0, 0, 0) 
        return S[1..n, 1..n]
    else
        return NULL

RLaberinto_numerico(T[1..n, 1..n], S[1..n, 1..n], i, j, p)
    if i < 0 or i > n or j < 0 or j > n // Estamos fuera del tablero
        return false

    if S[i,j] != 0 // Estamos en una casilla que ya hemos pasado
        return false
    
    if i = n and j = n //Estamos en la posicion final
        S[i,j] = p
        return true

    S[i,j] = p // Casilla visitada
    d = T[i,j] // Distancia a recorrer

    // Mover hacia arriba
    if RLaberinto_numerico(T[1..n, 1..n], S[1..n, 1..n], i - d, j, p + 1) 
        return true
    
    // Mover hacia abajo
    if RLaberinto_numerico(T[1..n, 1..n], S[1..n, 1..n], i + d, j, p + 1) 
        return true

    // Mover a la derecha
    if RLaberinto_numerico(T[1..n, 1..n], S[1..n, 1..n], i, j + 1, p + 1) 
        return true
    
    // Mover a la izquierda
    if RLaberinto_numerico(T[1..n, 1..n], S[1..n, 1..n], i, j - d, p + 1) 
        return true
        
    // Si nunguna funciona retornamos la casilla a 0
    S[i,j] = 0
    
    return false
    

