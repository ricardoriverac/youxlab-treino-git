import re
from time import sleep
frase = str(input('Digite uma frase: ').strip())
fraseLimpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
print('{}PROCESSANDO...{}'.format('\033[36m', '\033[m'))
while fraseLimpa != fraseLimpa[::-1]:
    print('Essa frase NÃO é um {}PALÍNDROMO{} \n {}Tente de novo{}'.format('\033[35m', '\033[m', '\033[33m','\033[m'))
    break
else:
    print('Essa frase é um {}PALÍNDROMO{}'.format('\033[35m', '\033[m'))
