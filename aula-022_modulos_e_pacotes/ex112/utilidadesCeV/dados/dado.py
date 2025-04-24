def metade(num, esco):
    metade = num / 2
    if esco == True:
        print(f'A metade de {num} é R${metade:.2f}')
        return '-=' *30
    else:
        if esco == False:
            print(f'A metade de {num} é {metade}')
            return '-=' *30


def dobro(num, esco):
    dobro = num * 2
    if esco == True:
        print(f'O dobro de {num} é R${dobro:.2f}')
        return '-=' *30
    else:
        if esco == False:
            print(f'O dobro de {num} é {dobro}')
            return '-=' *30

def aumentar(num, porcent, esco):
    taxa = (porcent/100) + 1
    aumento = num * taxa
    if esco == True:
        print(f'O aumento em {porcent} de {num} é R${aumento:.2f}')
        return '-=' *30
    else:
        if esco == False:
            print(f'O aumento em {porcent} de {num} é {aumento}')
            return '-=' *30

def diminuir(num, porcent, esco):
    tax = 1 - (porcent/100)
    diminuir = num * tax
    if esco == True:
        print(f'A diminuição de {porcent} de {num} é R${diminuir:.2f}')
        return '-=' *30
    else:
        if esco == False:
            print(f'A diminuição de {porcent} de {num} é {diminuir}')
            return '-=' *30

import json
import requests
def outraMoeda(num, conv):
    moeda = num
    tipo = conv
    real = num * 1
    dolar = num / 5.74
    if conv == 'D':
        print(f'O valor {moeda} convertido em dolar é USD {dolar:.2f}')
        return " "
    if conv == 'R':
        print(f'O valor {moeda} em reais é R${real}')
        return " "
        moeda = real
    if conv == 'B':
        moeda = int(num)
        binario = bin(moeda)
        print(f'Valor {num} em binário: {binario}')
        return " "
    else:
        if conv != "R" and conv != "D" and conv != 'B':
            return print('Erro não reconhecemos esse valor') == True



def resumo(num, porcent1, porcent2):
    dobro = num * 2
    metade = num / 2
    taxa = (porcent1/100) + 1
    aumento = num * taxa
    dimi = 1 - (porcent2/100)
    diminui = num * dimi
    print('-=' *30)
    print('        RESUMO DO VALOR          ')
    print('-=' *30)
    print(f'A metade de {num} é {metade}')
    print(f'O dobro de {num} é {dobro}')
    print(f'O aumento em {porcent1} de {num} é {aumento}')
    print(f'O valor reduzido em {porcent2} de num é {diminui}')
    print('-=' *30)



import re


def leia_dinheiro():
    while True:
        num = input('Digite um valor: R$').strip().replace(',', '.')
        if re.fullmatch(r'\d+(\.\d{1,2})?', num):
            return float(num)
        else:
            print(f'Erro: "{num}" não é um valor monetário válido. Tente novamente.')


