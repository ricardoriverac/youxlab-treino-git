#fazer
from random import randint
print('''Suas opções: 
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA ''')
computador= randint(1 , 3)
jogador= int(input('Qual é sua jogada? '))
if computador == 1 and jogador == 3:      
      print('Computador: {}\n Jogador: {}'.format(computador, jogador))
      print('Você perdeu!')

elif computador == 2 and jogador == 1:
      print('Computador: {}\n Jogador: {}'.format(computador, jogador))
      print('Você perdeu!')

elif computador == 3 and jogador == 2:    
     print('Computador: {}\n Jogador: {}'.format(computador, jogador))      
     print('Você perdeu!')

elif jogador == 1 and computador == 3:
      print('Computador: {}\n Jogador: {}'.format(computador, jogador))
      print('Você venceu!')

elif jogador == 2 and computador == 1:     
      print('Computador: {}\n Jogador: {}'.format(computador, jogador))
      print('Você venceu!')

elif jogador == 3 and computador == 2: 
      print('Computador: {}\n Jogador: {}'.format(computador, jogador))
      print('Você venceu!')

elif computador == jogador:
      print('Tente mais uma vez!')




