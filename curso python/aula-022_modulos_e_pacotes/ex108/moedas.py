def metade(num, esco):
    metade = num / 2
    if esco == "S":
        return print(f'A metade de {num} é R${metade:.2f}')
    else:
        if esco == "N":
            return print(f'A metade de {num} é R${metade:.2f}')


def dobro(num):
    dobro = num * 2
    return dobro


def aumentar(num, porcent):
    taxa = (porcent/100) + 1
    aumento = num * taxa
    return aumento

def diminuir(num, porcent):
    tax = 1 - (porcent/100)
    diminuir = num * tax
    return diminuir

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




    # moedx = 'USDBRL'
    # url = 'https://economia.awesomeapi.com.br/json/last/'+ moedx[0:3] +'-'+ moedx[3:6]
    # cotacao = requests.get (url).content
    # dic = json.loads(cotacao)
    # valorDolar = num / dic[moedx]["bid"]
    # # # return cotacao
    # # print(f'O valor {num} em dolar é {valorDolar}')
    # print(valorDolar)
    # print(f'Cotação: {dic[moedx]["bid"]}')
    







