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