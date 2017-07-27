largura = int(input("digite a largura: "))
altura  = int(input("digite a altura: "))

a = 0
while a < altura:
    l = 1
    c = ' '
    if(a == 0 or a == (altura - 1)):
        c = '#'
    print("#",end='')
    while l < largura - 1:
        print(c,end='')
        l = l + 1
    print('#')
    a = a + 1
    
