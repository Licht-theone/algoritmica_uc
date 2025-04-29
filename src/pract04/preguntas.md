## EJERCICIO 1 ##

    monedas_voraz(V[1..n], cantidad)
        Ordenar(V) //Ordena las monedas en funcion del valor (descendiente)
        MonedasSeleccionadas = [0,..,0]
        cantidadRestante <- cantidad
        
        while cantidadRestante > 0
            i <- 0
            foreach v -> v pertenece V[]
                if v <= cantidadRestante 
                    MonedasSeleccionadas[i] <- MonedasSeleccionadas[i] + 1
                    cantidadRestante <- cantidadRestante - v
                    break
                i <- i + 1
        
        return MonedasSeleccionadas


## EJERCICIO 2 ##
    //Array de memoización (inicialmente “no calculado”)
    para j desde 0 hasta n hacer
        memo[j] ← –1
    fin para
    memo[0] ← 0   // caso base: 0 monedas para cambiar 0 unidades

    //Función recursiva con memoización
    función C(j):
        si memo[j] ≠ –1 entonces
            return memo[j]
        fin si

        minC ← ∞
        para i desde 1 hasta m hacer
            si V[i] ≤ j entonces
                c ← 1 + C(j – V[i])
                si c < minC entonces
                    minC ← c
                fin si
            fin si
        fin para

        memo[j] ← minC
        return minC
    fin función


    return C(n)


## EJERCICIO 3 ##

    monedas_bottom-up(V[1..n], cantidad):
        A[1..cantidad, 0..n] <- ([0,..,0] , [0,..,0])
        
        for i <- 1 to cantidad
            for j <- 1 to n
                if V[i] > j
                    A[i, j] ← A[i – 1, j]
                else
                    A[i, j] ← min {A[i – 1, j], A[i, j – V[i]] + 1}
    
        i ← m; j ← n
        listaMonedas ← []
        while i ≥ 1 y j > 0:
            if A[i][j] = A[i-1][j]
            // no usamos ninguna moneda de valor V[i]
                i ← i − 1
            else
                añadir V[i] a listaMoneda
                j ← j − V[i]
        return listaMonedas