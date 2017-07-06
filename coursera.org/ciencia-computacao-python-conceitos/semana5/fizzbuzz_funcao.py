def ehDividivelPor(iNumero, iDivisor):
    if(iNumero % iDivisor == 0):
        return True
    return False

def fizzbuzz(iNumero):
    if(type(iNumero) != int):
        return iNumero
    ehDividivelPor3 = ehDividivelPor(iNumero,3)
    ehDivisivelPor5 = ehDividivelPor(iNumero,5)
    if(ehDividivelPor3 and not ehDivisivelPor5):
        return "Fizz"
    if(not ehDividivelPor3 and ehDivisivelPor5):
        return "Buzz"
    if(ehDividivelPor3 and ehDivisivelPor5):
        return "FizzBuzz"
    return iNumero

iNumero = int(input("Entre com o valor: "))
print(fizzbuzz(iNumero))

    
