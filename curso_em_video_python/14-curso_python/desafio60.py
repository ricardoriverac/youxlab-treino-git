from time import sleep
from math import factorial

print('Digite um número e veja seu fatorial: ')

numero = int(input('Digite o número: '))
c = numero
f = factorial(numero)

while c > 0:
    print('{} x '.format(c), end=' ')
    c -= 1
    if c ==1:
       print('{} ='.format(c))
       print('\033[1;31mCALCULANDO {}! \033[0;0m'.format(numero))
       sleep (2)
       print('O fatorial de {} é {}'.format(numero, f))
       