import math

iX1 = int( input( "Entre com o valor de X da primeira coordenada: " ) )
iY1 = int( input( "Entre com o valor de Y da primeira coordenada: " ) )

iX2 = int( input( "Entre com o valor de X da segunda coordenada: " ) )
iY2 = int( input( "Entre com o valor de Y da segunda coordenada: " ) )

fDistancia = math.sqrt( ( iX2 - iX1 ) ** 2 + ( iY2 - iY1 ) ** 2 )

if( fDistancia >= 10 ):
    print( "longe" )
else:
    print( "perto" )
    
