iNumero = int( input( "Entre com um número inteiro: " ) )
if( not iNumero  % 3  and not iNumero % 5 ):
    print( "FizzBuzz" )
else:
    print( iNumero )
    
