from time import sleep
from random import randint
cont = 0
soma = 0
escolha = ""
print('¨=¨' * 15)
print('vamos jogar par ou impar')
print('¨=¨' * 15)
sleep(0.1)
while True:
    computador = randint(0, 10)
    jogador = int(input('digite um numero: '))
    escolha = str(input('Par / Impar ')).strip().upper()[0]
    soma = jogador + computador
    if escolha in 'Pp':
        if soma % 2 == 0:
            sleep(1)
            print('voce venceu')
            cont += 1
        else:
            sleep(1)
            print('voce perdeu')
            print('-' * 20)
            print(f'seu número vitorias de vitorias é {cont}')
            print('-' * 20)
            break
    elif escolha in 'Ii':
        if soma % 2 == 1:
            sleep(1)
            print('voce venceu')
        else:
            sleep(1)
            print('voce perdeu')
            print('-=' * 20)
            print(f'seu números de vitorias é {cont} ')
            print('-=' * 20)
            break
