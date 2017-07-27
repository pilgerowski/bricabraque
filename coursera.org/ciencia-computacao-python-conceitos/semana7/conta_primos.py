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

def n_primos(n):
    if(n < 2):
        return 0
    primo = 2
    conta = 1
    while primo < n:
        primo = proximoPrimo(primo)
        if(primo <= n):
            conta = conta + 1
    return conta

print("Quantidade de primos entre 2 e n:")
nums = range(1, 100)
for n in nums:
    print("n = ", n, " número de primos: ", n_primos(n))
    
