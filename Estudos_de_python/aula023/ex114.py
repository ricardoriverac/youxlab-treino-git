import requests

try: 
    site = requests.get('http://www.pudim.com.br')
    print(site.text)

except:
    print('Deu Erro ')

else:
    print('Tudo OK ')






