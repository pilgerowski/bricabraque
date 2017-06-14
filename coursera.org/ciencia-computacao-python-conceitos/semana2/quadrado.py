#!/usr/local/bin/python
#coding: utf-8
import os, sys

iLadoQuadrado = int(input("Digite o valor correspondente ao lado de um quadrado: "))
iPerimetro = iLadoQuadrado * 4
iArea = iLadoQuadrado ** 2
print("perímetro: {} - área: {}".format(iPerimetro, iArea))
