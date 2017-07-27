def maior_elemento( aLista ):
    aLista.sort()
    return aLista[-1]

a=[434,467,572,743,834,176]
print(maior_elemento(a))
