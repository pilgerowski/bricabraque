def remove_repetidos( aLista ):
    aLista.sort()
    anterior = aLista.pop(0)
    novaLista = [ anterior ]
    for item in aLista:
        if( not( item == anterior ) ):
            novaLista.append( item )
        anterior = item     
    return novaLista
         
