import urllib
import urllib.error
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Nõa funcionou, site não esta acessivel.')
else:
    print('Deu certo, o site está acessive.l')