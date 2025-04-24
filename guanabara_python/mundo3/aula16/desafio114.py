import requests

def URLvalida(url):
    if not url.startswith('https://'):
        url = 'https://' + url

    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f'O site \033[1;32m{url}\033[m está acessível.')
        else:
            print(f'O site \033[33m{url}\033[m respondeu com status {resposta.status_code}.')
    except requests.exceptions.RequestException as e:
        print(f'O site \033[31m{url}\033[m não está acessível.')
        print(f'Erro: {e}')

url = input('Digite a URL: ').strip().lower()
URLvalida(url)
