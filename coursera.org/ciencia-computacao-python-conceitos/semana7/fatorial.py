def fatorial(n):
    if(n > 1):
        return n * fatorial(n-1)
    return 1

x = 0
while x >= 0:
    x = int(input("Entre com o valor desejado: "))
    print("O fatorial é ", fatorial(x))

