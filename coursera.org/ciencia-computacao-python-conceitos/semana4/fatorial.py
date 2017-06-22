bNatural = False;
while not bNatural:
    iNumero = int(input("Digite o valor de n: "))
    bNatural = ( iNumero >= 0 )

iFatorial = 1
while iNumero > 1:
    iFatorial = iFatorial * iNumero
    iNumero = iNumero - 1

print(iFatorial)
