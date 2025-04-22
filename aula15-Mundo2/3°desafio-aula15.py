#PAR OU ÍMPAR?
from random import randint
vitorias=0
print('QUER JOGAR PAR OU ÍMPAR?')
while True:
    jogador=int(input('Digite um número:'))
    computador=randint(1,10)
    total=jogador+computador
    escolha=' '
    while escolha not in 'PI':
        escolha=str(input('Par ou Ímpar?[P/I]:')).strip().upper()[0]
    print(f'Você jogou o número {jogador} e o computador jogou o número {computador}. Total de {total} ')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            vitorias+=1
        else:
            print('Você PERDEU!!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            vitorias+=1
        else:
            print('Você PERDEU!!')
            break
print(f'ACABOU!Você venceu {vitorias} vezes.')