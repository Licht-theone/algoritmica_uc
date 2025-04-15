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


## EJERCICIO 3 ##

    monedas_bottom-up(V[1..n], cantidad):
        A[1..cantidad, 0..n] <- ([0,..,0] , [0,..,0])
        
        for i <- 1 to cantidad
            for j <- 1 to n
                if V[i] > j
                    A[i, j] ← A[i – 1, j]
                else
                    A[i, j] ← min {A[i – 1, j], A[i, j – V[i]] + 1}
        // TODO: el resto
        