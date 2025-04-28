from random import choice
import random
print('Vamos jogar Jo Ken Po!!!')
print('<=>'*15)
suaEscolha=input(str('Escolha pedra,papel ou tesoura: '))
opcoes=('pedra','papel','tesoura')
computador=random.choice(opcoes)
print('O seu adversário escolheu: {}'.format(computador)) 

if suaEscolha == 'pedra' and computador == 'tesoura' or suaEscolha == 'tesoura' and computador == 'papel' or suaEscolha == 'papel' and computador == 'pedra':
    print('Parabéns você ganhou!!! ')

elif suaEscolha == computador:
    print('Temos um empate!!! ')

else:
    print('A máquina ganhou!!! ')





