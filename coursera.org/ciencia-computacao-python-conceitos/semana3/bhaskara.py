import math

fA = float( input( "Entre com o valor do coeficiente A: " ) )
fB = float( input( "Entre com o valor do coeficiente B: " ) )
fC = float( input( "Entre com o valor do coeficiente C: " ) )

fDelta = fB ** 2 - 4 * fA * fC

if( fDelta < 0 ):
    print( "esta equação não possui raízes reais" )
else:
    fX1 = ( - fB + math.sqrt( fDelta ) ) / ( 2 * fA )
    if( fDelta == 0 ):
        print( "a raiz desta equação é {}".format( fX1 ) )
    else:
        fX2 = ( - fB - math.sqrt( fDelta ) ) / ( 2 * fA )
        if( fX2 < fX1 ):
            fAux = fX1
            fX1 = fX2
            fX2 = fAux
        print( "as raízes da equação são {} e {}".format( fX1, fX2 ) )
        
