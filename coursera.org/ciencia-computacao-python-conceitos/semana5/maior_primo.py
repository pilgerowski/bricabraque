import math

def ehPrimo(iNumero):
    # é primo todo número natural divisível por 1 e por ele mesmo, sendo
    # que 0, 1 e números negativos não são considerados primos
    if(type(iNumero) != int | iNumero < 2):
        return False
    
    # 2 é o único número par primo
    if(iNumero == 2):
        return True
    if(iNumero % 2 == 0):
        return False

    iImpar = 1
    iSqrt_n = int(math.sqrt(iNumero))
    while True:
        iImpar = iImpar + 2
        if(iNumero % iImpar == 0):
            return False
        if(iImpar > iSqrt_n):
            break
    return True

def maiorPrimo(iNumero):
    if(type(iNumero) == int & iNumero >= 2):
        for iMaior in range(iNumero,1,-1):
            if(ehPrimo(iMaior)):
                return iMaior
    return False;

iNumero = input("Entre com o valor:")
print(maiorPrimo(iNumero))
        
        
