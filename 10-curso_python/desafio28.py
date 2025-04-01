from random import randint
numero = int(input('Tente advinhar o número que estou pensando, digite um número de 0 a 5: '))
numeroQueEuQuero = randint(0, 5)
if numero == numeroQueEuQuero :
    print('Vocẽ acertou, nossa.')
else :
    print('MUHAHAHA, vocẽ errou! Pensei no número {} e não em {}'.format(numeroQueEuQuero, numero))