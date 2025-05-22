import random
numero = random.randint(0, 10)
jogada = int(input('Adivinhe o número que estou pensando entre 0 e 10: '))
cont = 1
while jogada != numero:
    if jogada > numero:
        print('Informe um valor menor...')
    elif jogada < numero:
        print('Informe um valor maior...')
    jogada = int(input('Tente novamente: '))
    cont += 1
print(f'Parabéns, com {cont} tentativas você venceu!!!')