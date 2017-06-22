iNumero = int(input("Digite um número inteiro: "))

iSoma = 0
while iNumero > 0:
    iSoma = iSoma + ( iNumero % 10 )
    iNumero = iNumero // 10

print(iSoma)
