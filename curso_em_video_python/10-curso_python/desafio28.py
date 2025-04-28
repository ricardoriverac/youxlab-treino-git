from random import randint
from time import sleep
numero = int(input('Tente advinhar o número que estou pensando, digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
numeroQueEuQuero = randint(0, 5)
if numero == numeroQueEuQuero :
    print('Vocẽ acertou, nossa.')
else :
    print('MUHAHAHA, vocẽ errou! Pensei no número {} e não em {}'.format(numeroQueEuQuero, numero))