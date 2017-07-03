def ehVogal(sPalavra):
    sLetra = sPalavra[0].capitalize()
    aVogais = ["A", "E", "I", "O", "U"]
    if sLetra in aVogais:
        return True
    return False

sLetra = input("Entre com o caracter: ")
print(ehVogal(sLetra))
