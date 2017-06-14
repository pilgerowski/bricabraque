#!/usr/local/bin/python
#coding: utf-8
import os, sys

iNumero = int( input( "Digite um número inteiro: " ) )

iDezena = ( iNumero // 10 ) % 10

print( "O dígito das dezenas é {}".format(iDezena) )
