
import json
import requests
def dolarapi(num):
    moedx = 'USDBRL'
    url = 'https://economia.awesomeapi.com.br/json/last/'+ moedx[0:3] +'-'+ moedx[3:6]
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dic = json.loads(resposta.content)
        # cotacao = requests.get (url).content
        valorDolar = float(dic[moedx]["bid"])
        valDolar = num / valorDolar
        print(f'{valDolar:.2f}')

    else:
        print('Erro ao acessar a api')

    # valor = int(dic[moedx]["bid"])
    # valorDolar = num / dic[moedx]["bid"]
    # # return cotacao
    # print(f'O valor {num} em dolar é {valorDolar}')
    # print(valorDolar)
    # print(f'Cotação: {valor + num}')