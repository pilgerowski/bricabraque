iNumero = int(input("Digite um número inteiro: "))

bHaAdjacenteIgual = False
iAnterior = iNumero % 10
while(iNumero > 0):
    iNumero = iNumero // 10
    iDigito = iNumero % 10
    if(iDigito == iAnterior):
        bHaAdjacenteIgual = True
    iAnterior = iDigito
if(bHaAdjacenteIgual):
    print("sim")
else:
    print("não")
