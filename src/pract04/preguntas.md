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

monedas_topdown(V[1..m], n):
    for j ← 0 to n:
        for i ← 1 to m:
            M[j, i] ← NULL
    return CAMBIO_TD(n, m)

rec_monedas_topdown(j, i):
    //Casos base
    if j = 0 then
        return 0

    if i = 1 then
        return j       // necesitamos j monedas de valor 1

    if M[j, i] ≠ NULL then
        return M[j, i]

    if V[i] > j then / no podemos usar la moneda V[i]
        M[j, i] ← rec_monedas_topdown(j, i−1)
    else
        M[j, i] ← min(CAMBIO_TD(j, i−1), 1 + CAMBIO_TD(j−V[i], i))

    return M[j, i]


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