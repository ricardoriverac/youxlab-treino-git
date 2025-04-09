from random import randint
computador = randint(0, 10)
print('Sou eu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    if jogador == computador:
        acertou = True
print('Acertou!')