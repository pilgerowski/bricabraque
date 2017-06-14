#!/usr/local/bin/python
#coding: utf-8
import os, sys

iNota1 = int(input("Digite a primeira nota: "))
iNota2 = int(input("Digite a segunda nota: "))
iNota3 = int(input("Digite a terceira nota: "))
iNota4 = int(input("Digite a quarta nota: "))

fMedia = ( iNota1 + iNota2 + iNota3 + iNota4 ) / 4.0

print("A média aritmética é {}".format(fMedia))
