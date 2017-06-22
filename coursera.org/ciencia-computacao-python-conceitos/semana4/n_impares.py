bNatural = False
while not bNatural:
    iNumero = int(input("Digite o valor de n: "))
    bNatural = ( iNumero > 0 )

iImpar = 1
while iNumero > 0:
    print(iImpar)
    iImpar = iImpar + 2
    iNumero = iNumero - 1
    
