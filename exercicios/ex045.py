#fazer
from random import randint
itens= ('Pedra, Papel, Tesoura')
print('''Suas opções: 
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA ''')
computador= randint(1 , 3)
jogador= int(input('Qual é sua jogada? '))
print('Computador jogou {}'.itens[computador])
print('Jogador jogou {}'.itens[jogador])