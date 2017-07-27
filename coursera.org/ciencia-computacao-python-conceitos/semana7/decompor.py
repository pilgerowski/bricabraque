import math

def ehPar(x):
    return ( x % 2 == 0 )

def ehPrimo(x):
    if(x == 2 | x == 3):
        return True
    if( ehPar(x) ):
        return False
    impares = range(5, int(math.sqrt(x)), 2)
    for n in impares:
        if(x % n == 0):
            return False
    return True
    
def proximoPrimo(n):
    if(n == 1):
        return 2
    else:
        if(n == 2):
            return 3
    if( ehPar(n) ):
        impar = n + 1
    else:
        impar = n + 2
    while not ehPrimo(impar):
        impar = impar + 2
    return impar
    
def multiplicidade(n, fator):
    m = 0
    while n % fator == 0:
        m = m + 1
        n = n / fator
    return m

def decompor(n):
    x = 1
    primo = 2
    while primo <= n:
        m = multiplicidade(n,primo)
        if(m > 0):
            print("Fator",primo,"multiplicidade =",m)
            x = x * (primo ** m)
            if(x == n):
                return
        primo = proximoPrimo(primo)
    return

x = 2
while x > 1:
    x = int(input("Digite um número inteiro maior que 1: "))
    decompor(x)
