from random import randint
numero = randint(0,5)
usuario = int(input('Escolha um número inteiro entre 0 e 5: '))
if usuario == numero:
    print('Você venceu, PARABÉNS!')
else:
    print('Você perdeu, MELHORE!')