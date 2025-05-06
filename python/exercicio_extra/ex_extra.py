#jokenpô com 3 pessoas
jogador1= 0
jogador2= 0
jogador3= 0
jogo= []
print('='*40)
print('JOKENPÔ COM 3 JOGADORES')
print('='*40)
while True:
    print('''Suas opções: 
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA ''')
    jogador1= int(input('Qual é sua escolha? '))
    jogador2= int(input('Qual é sua escolha? '))
    jogador3= int(input('Qual é sua escolha? '))
    if jogador1== jogador2 and jogador2== jogador3 and jogador1== jogador3:
        print('EMPATE!')
        #se o vencedor for pedra
    else:
        if jogador1== 1 and jogador2 ==1 and jogador3 ==3:
         print('Jogador 3 perdeu. Os jogadores 1 e 2 venceram!')
        if jogador2 == 1 and jogador3 ==1 and jogador1 ==3:
            print('Jogador 1 perdeu. Os jogadores 2 e 3 venceram!')
            if jogador3==1 and jogador1== 1 and jogador2==3:
                print('Jogador 2 perdeu. Os jogadores 1 e  venceram!')
        #se o vencedor for papel
        if jogador1== 2 and jogador2 ==2 and jogador3 ==1:
            print('Jogador 3 perdeu. Os jogadores 1 e 2 venceram!')
            if jogador2 == 2 and jogador3 ==2 and jogador1 ==1:
                print('Jogador 1 perdeu. Os jogadores 2 e 3 venceram!')
                if jogador3==2 and jogador1== 2 and jogador2==1:
                    print('Jogador 2 perdeu. Os jogadores 1 e  venceram!')
        #se o vencedor for tesoura
        if jogador1== 3 and jogador2 ==3 and jogador3 ==1:
            print('Jogador 3 perdeu. Os jogadores 1 e 2 venceram!')
        if jogador2 == 3 and jogador3 ==3 and jogador1 ==1:
            print('Jogador 1 perdeu. Os jogadores 2 e 3 venceram!')
        if jogador3==3 and jogador1== 3 and jogador2==1:
            print('Jogador 2 perdeu. Os jogadores 1 e  venceram!')
        