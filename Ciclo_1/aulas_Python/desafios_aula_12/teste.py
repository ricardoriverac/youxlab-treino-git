#Desafio: Crie um programa que faça o computador jogar JOKENPÔ com você.
from random import choice      #Eu tinha usado o randint mas ele só serve para números ... para isso, tenho o choice para strings

print ('\033[1;34;40mVamos jogar PEDRA, PAPEL E TESOURA?\033[m')

opções = ['Pedra', 'Papel', 'Tesoura']

computador = choice(opções)

jogador = str(input('Escolha uma das opções (Pedra, Papel ou Tesoura:)')) .capitalize()  #Usei o método capitalize para garantir que a entrada do jogador seja comparável independente da capitalização

if jogador not in opções:
    print('\033[1;31;40mVocê não escolheu uma das opções ... Tá com medinho?\033[m')
else:
    print(f'Eu escolhi {computador} e você escolheu {jogador}')
    if jogador == computador:
        print('\033[1;30;40mEMPATE!\033[m')
    elif (jogador == 'Pedra' and computador == 'Tesoura') or \
    (jogador == 'Papel' and computador == 'Pedra') or \
    (jogador == 'Tesoura' and computador == 'Papel'):
        print('\033[1;32;40mVOCÊ VENCEU!\033[m')
    else:
        print('\033[1;31;40mVOCÊ PERDEU!\033[m')