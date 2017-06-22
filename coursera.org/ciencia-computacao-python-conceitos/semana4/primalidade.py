import math

bNatural = False
while not bNatural:
    iNumero = int(input("Digite um número inteiro: "))
    bNatural = ( iNumero >= 0 )

bPrimo = True
if iNumero == 0 | iNumero == 1:
    bPrimo = False
else:
    iConta = int(math.sqrt(iNumero))
    while(iConta > 1):
        if(iNumero % iConta == 0):
            bPrimo = False
        iConta = iConta - 1

if(bPrimo):
    print("primo")
else:
    print("não primo")
    
