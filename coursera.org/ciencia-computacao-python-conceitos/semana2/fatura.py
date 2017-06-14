#!/usr/local/bin/python
#coding: utf-8
import os, sys

sNomeCliente = input("Digite o nome do cliente: ")
sDiaVencimento = input("Digite o dia de vencimento: ")
sMesVencimento = input("Digite o mês de vencimento: ")
sValorFatura = input("Digite o valor da fatura: ")

print("Olá, {}".format(sNomeCliente))
print("A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(sDiaVencimento, sMesVencimento, sValorFatura))

