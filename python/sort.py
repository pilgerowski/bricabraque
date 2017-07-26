def ordena(aLista):
    numElementosDaLista = int(len(aLista))
    if( numElementosDaLista > 1 ):
        indiceInicioLista =  0
        indiceFinalLista  = -1
        for i in range(numElementosDaLista):                
            if(aLista[i] > aLista[indiceFinalLista]):                
                aLista[i], aLista[indiceFinalLista]   = aLista[indiceFinalLista], aLista[i]
            if(aLista[i] < aLista[indiceInicioLista]):
                aLista[i], aLista[indiceInicioLista] = aLista[indiceInicioLista], aLista[i]
        maiorValor = aLista.pop(indiceFinalLista)
        menorValor = aLista.pop(indiceInicioLista)
        return [menorValor] + ordena(aLista) + [maiorValor]     
    else:
        return aLista
    
a = [343,47,9,8,5,4,3,6,2,1,9]
print(a)
b = ordena(a)
print(b)
