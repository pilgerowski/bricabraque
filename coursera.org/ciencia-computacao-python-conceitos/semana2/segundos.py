#!/usr/local/bin/python
#coding: utf-8
import os, sys

iSegundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

iNumeroSegundosMinuto = 60
iNumeroSegundosHora = iNumeroSegundosMinuto * 60
iNumeroSegundosDia = iNumeroSegundosHora * 24

iDias = iSegundos // iNumeroSegundosDia
iSegundos = iSegundos - ( iDias * iNumeroSegundosDia )

iHoras = iSegundos // iNumeroSegundosHora
iSegundos = iSegundos - ( iHoras * iNumeroSegundosHora )

iMinutos = iSegundos // iNumeroSegundosMinuto
iSegundos = iSegundos - ( iMinutos * iNumeroSegundosMinuto )

print("{} dias, {} horas, {} minutos e {} segundos.".format(iDias, iHoras, iMinutos, iSegundos))


