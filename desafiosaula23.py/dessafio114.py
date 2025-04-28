import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento!\033[m ')
else:
    print('\033[33mO site pudim está acessível no momento!\033[m ')
    
