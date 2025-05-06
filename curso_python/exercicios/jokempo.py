import random
print ('Vamos jogar Jokempô! ')
nome1 = str(input('Digite o nome de um(a) jogador(a): '))
nome2 = str(input('Digite o nome de outro(a) jogador(a): '))
opcoes = ('Pedra', 'Papel', 'Tesoura')
print (f"""{nome1}, faça sua escolha:
       [ 0 ] - Pedra
       [ 1 ] - Papel
       [ 2 ] - Tesoura""")
jogador1 = int(input('Qual você escolheu? '))
print (f"""{nome2}, faça sua escolha:
       [ 0 ] - Pedra
       [ 1 ] - Papel
       [ 2 ] - Tesoura""")
jogador2 = int(input('Qual você escolheu? '))
computador = random.randint(0, 2)
# empate
if computador == jogador1 and computador == jogador2 and jogador1 == jogador2:
    print (f'O computador e os(as) jogadores(as) jogaram {computador}. Ou seja, EMPATE!')

# computador ganha de todos
elif (computador == 0 and jogador1 == 2) or (computador == 0 and jogador2 == 2):
    print (f'O computador jogou {computador} e os(as) jogadores(as) jogaram {jogador1} e {jogador2}. Ou seja, O COMPUTADOR VENCEU! ')
elif (computador == 1 and jogador1 == 0) or (computador == 1 and jogador2 == 0):
    print (f'O computador jogou {computador} e os(as) jogadores(as) jogaram {jogador1} e {jogador2}. Ou seja, O COMPUTADOR VENCEU! ')
elif (computador == 2 and jogador1 == 1) or (computador == 2 and jogador2 == 1):
    print (f'O computador jogou {computador} e os(as) jogadores(as) jogaram {jogador1} e {jogador2}. Ou seja, O COMPUTADOR VENCEU! ')

# computador ganha do jogador 1 e continua a jogar com o jogador 2
elif (computador == 0 and jogador1 == 2) or (computador == 1 and jogador1 == 0) or (computador == 2 and jogador1 == 1):
    print (f"""O computador jogou {computador}, o(a) jogador(a) {nome1} jogou {jogador1} e o(a) jogador(a) {nome2} jogou {jogador2}. 
           Ou seja, o computador VENCE de {nome1}, PORÉM continua jogando com {nome2}!""" )

# computador ganha do jogador 2 e continua jogando com o jogador 1
elif (computador == 0 and jogador2 == 2) or (computador == 1 and jogador2 == 0) or (computador == 2 and jogador2 == 1):
    print (f"""O computador jogou {computador}, o(a) jogador(a) {nome2} jogou {jogador2} e o(a) jogador(a) {nome1} jogou {jogador1}. 
           Ou seja, o computador VENCE de {nome2}, PORÉM continua jogando com {nome1}!""")