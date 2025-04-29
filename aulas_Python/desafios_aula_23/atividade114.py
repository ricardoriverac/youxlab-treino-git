import requests

url = "https://www.pudim.com.br" 

try:
    response = requests.get(url)
    response.raise_for_status() 

    if response.status_code == 200:
        print('\033[32mConsegui acessar o site do pudim com sucesso!\033[m')
except:
    print('\033[31mO site do Pudim não está acessível no momento\033[m')