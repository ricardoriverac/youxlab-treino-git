import random

computador= random.randint(1, 5)

numero= int(input('Palpite, um número de 1 a 5: '))
if computador == numero:
    print('Você venceu!')
else:
    print('Você perdeu!')