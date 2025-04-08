from random import randint
from time import  sleep
print('Vamos jogar Jokempo?')
print('faça a sua escolha...')
itens = ('pedra','papel','tesoura')
computador = randint(1 , 2)
print('''
[1]Pedra
[2]Papel
[3]Tesoura''')
jogador = int(input('Escolha uma opção: '))
print('Jokempo')
if computador == 1:  
    if jogador == 1
        print('Temos um empate')
        print('Eu escolhi Pedra e você escolheu Pedra')
elif jogador == 2:
        print('Ganhou')
        print('Eu escolhi Pedra e você escolheu Papel ')
elif jogador == 3:     
        print('Perdeu')
        print('Eu escolhi Pedra e você escolheu Tesoura')
elif computador == 2:
    if jogador == 1: 
        print('Você perdeu')
        print('Eu escolhi Papel e você escolheu Pedra')
elif jogador == 2: 
        print('empate')
        print('Eu escolhi Papel e você escolheu Papel')
elif jogador == 3: 
        print('Você ganhou')
        print('Eu escolhi Papel e você escolheu Tesoura')
elif computador == 3:       
    if jogador == 1:        
        print('Você Ganhou')
        print('Eu escolhi Tesoura e você escolheu Pedra')
elif jogador == 2:    
        print('Você Perdeu')
        print('Eu escolhi Tesoura e você escolheu Papel')
elif jogador == 3:     
        print('Temos um empate')
        print('Eu escolhi Tesoura e você escolheu Tesoura')