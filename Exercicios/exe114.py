# Crie um código em python que teste se o site pudim está acessivel pelo computador usado.

import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessivel no momento.")
else:
    print("Consegui acessar o site Pudim com sucesso.")