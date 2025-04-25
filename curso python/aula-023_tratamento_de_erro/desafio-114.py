import requests
def site_no_ar(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False


url = 'https://www.pudim.com.br/'
if site_no_ar(url):
    print('O site está acessível.')
else:
    print("O site está fora do ar")
