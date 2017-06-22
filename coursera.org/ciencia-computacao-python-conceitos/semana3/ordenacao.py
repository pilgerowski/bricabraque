iNum1 = int( input( "Entre com o primeiro inteiro: " ) )
iNum2 = int( input( "Entre com o segundo inteiro: " ) )
iNum3 = int( input( "Entre com o terceiro inteiro: " ) )

if( iNum1 < iNum2 and iNum2 < iNum3 ):
    print( "crescente" )
else:
    print( "não está em ordem crescente" )
