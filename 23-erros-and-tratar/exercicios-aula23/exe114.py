import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://term.ooo/')
except:
    print('\033[31mO jogo termo está indisponivel no momento\n volte mais tarde!\033[m')
else:
    print('\033[32mO jogo termo está disponivel no momento\033[m')