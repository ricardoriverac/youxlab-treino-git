from random import randint
computador = randint(0,5)
usuario = int(input('Escolha um número inteiro entre 0 e 5: '))
if usuario == computador:
    print('Você venceu, PARABÉNS!')
else:
    print('Você perdeu, MELHORE!')