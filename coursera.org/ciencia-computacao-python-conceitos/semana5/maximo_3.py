def maximo_2(a, b):
    if(a > b):
        return a
    return b

def maximo_3(a, b, c):
    return maximo_2(a, maximo_2(b, c))

a = int(input("Entre com o valor de a:"))
b = int(input("Entre com o valor de b:"))
c = int(input("Entre com o valor de c:"))

print(maximo_3(a,b,c))
