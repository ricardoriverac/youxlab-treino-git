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
       if jogador1 != jogador2 and jogador3:
           print(jogador1)