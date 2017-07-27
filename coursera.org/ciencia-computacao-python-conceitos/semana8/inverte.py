def inverte( aLista ):
    novaLista = []
    for item in aLista:
        novaLista.insert( 0, item )
    return novaLista

n = 1
lista = [ ]
while( n > 0 ):
    n = int( input( "Digite um número: " ) )
    if( n > 0 ):
        lista.append( n )
print( ) 
for item in inverte( lista ):
    print( item )
