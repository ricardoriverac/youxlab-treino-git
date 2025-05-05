#esse eu nao consegui fazer usei chat
import requests
def testar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f"O site {url} está acessível!")
        else:
            print(f"O site respondeu com o status: {resposta.status_code}")
    except requests.ConnectionError:
        print("Erro de conexão. O site não está acessível.")
    except requests.Timeout:
        print("O tempo de conexão esgotou.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
testar_site("http://www.pudim.com.br")
