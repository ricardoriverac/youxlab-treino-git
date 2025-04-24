from random import randint
cont = 0
s = 0 
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor: '))
    opcao = str(input('Par ou Impar [P/I] ')).upper().strip()
    s = computador + jogador
    if (jogador + computador) % 2 == 0 and opcao == 'P' :
        print('-'*20)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU PAR')
        print('_'*30)
        print('Você venceu!')
        print('^'*30)
        cont += 1
    elif (jogador + computador) % 2 == 1 and opcao == 'I':
        print('-'*20)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU IMPAR')
        print('_'*30)
        print('Você venceu! ')
        print('^'*30)
        cont += 1
    else:
        break
print('-'*40)
print(f'GAME OVER! Você venceu apenas {cont} vezes')