def ordena(aLista):

    def maior(a, b):
        if( a > b ):
            return a
        return b

    def menor(a, b):
        if( a < b ):
            return a
        return b
    
    numElementosDaLista = int(len(aLista))
    if( numElementosDaLista < 2 ):
        return aLista
    else:
        indiceMenorValor = 0
        indiceMaiorValor = numElementosDaLista - 1
        menorValor = aLista[indiceMenorValor]
        maiorValor = aLista[indiceMaiorValor]
           
        for i in range(0,numElementosDaLista):
            menorValor = menor(aLista[i], menorValor)
            maiorValor = maior(aLista[i], maiorValor)
                
            if(aLista[i] == menorValor):                
                indiceMenorValor = i
            if(aLista[i] == maiorValor):
                indiceMaiorValor = i
           
        aLista.pop(maior(indiceMenorValor,indiceMaiorValor))
        aLista.pop(menor(indiceMenorValor,indiceMaiorValor))

    return [menorValor] + ordena(aLista) + [maiorValor]

a = [343,47,9,8,5,4,3,6,2,1,9]
print(a)
b = ordena(a)
print(b)
