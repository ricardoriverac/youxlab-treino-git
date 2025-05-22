import requests

def testar_site_pudim():
    url = "http://pudim.com.br"
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print("O site pudim está acessível!")
        else:
            print(f"O site respondeu com o código de status: {resposta.status_code}")
    except requests.ConnectionError:
        print("Não foi possível se conectar ao site pudim.")
    except requests.Timeout:
        print("A conexão com o site pudim expirou.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa o teste
testar_site_pudim()
