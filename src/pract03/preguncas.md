## PREGUNTA 1

Teniendo el código de la práctica es copiar y pegar, el EsSencillo sería la condición del primer if y Directo sería la función Mostrar. F(x) tiene que variar la m quedando m = m + 1 ya que es de lo 
que depende el EsSencillo. Diría yo que también tiene que variar A[hueco] y A[ficha] como hace en el código, intercambiandose. Lo último es la función c(x, y) pero va a ser sumar 1 al resultado y 
cambiar los "argumentos" de la función, cambiar en cada iteración los valores hueco y ficha siguiendo las formulas y condiciones del código. Para ver las posiciones del juego habrá que meter también los
Mostrar en cada iteración del bucle que tiene la función c.

## Pseudocodigo ITERATIVO

Iterativo(A, hueco, ficha, m):
	
	Y <- 0
	
	while not (m <= len(a) - 2) //EsSencillo(x)
		Mostrar(A)
		A[hueco], A[ficha] = A[ficha], A[hueco] 	
		
		if ficha = n + 1 
			m <== m + 1 
			
		if n <= ficha <= n +2  
			m <== m + 1 
	
		
		if hueco - 1 <= ficha <= hueco + 1
			nuevo_hueco <- ficha
			nueva_ficha <- hueco - A[hueco]
		
		else if A[hueco] == A[ficha + A[hueco]]
			nuevo_hueco <- ficha
			nueva_ficha <- hueco + A[hueco]
		else
			nuevo_hueco <- ficha
			nueva_ficha <- hueco + A[hueco]	* 2
	
		hueco <- nuevo_hueco
		ficha <- nueva ficha
		y <- y + 1 
	
	print A[1..2n+1]
	return y


## PREGUNTA 2

Iterativo(A, hueco, ficha, m):
	
	Y <- 0
    pila <- Pila()
	
	while not (m <= len(a) - 2) //EsSencillo(x)	
		if ficha = n + 1 
			m <== m + 1 
			
		if n <= ficha <= n +2  
			m <== m + 1 
	
		
		if hueco - 1 <= ficha <= hueco + 1
			nuevo_hueco <- ficha
			nueva_ficha <- hueco - A[hueco]
		
		else if A[hueco] == A[ficha + A[hueco]]
			nuevo_hueco <- ficha
			nueva_ficha <- hueco + A[hueco]
		else
			nuevo_hueco <- ficha
			nueva_ficha <- hueco + A[hueco]	* 2
	
		hueco <- nuevo_hueco
		ficha <- nueva ficha

        Apila(hueco, ficha, P)
	Mostrar(A)

    while pila not empty:
        hueco, ficha <- Desapila(P)
        A[hueco], A[ficha] = A[ficha], A[hueco] 
        Mostrar(A)

        y <- y + 1

	return y