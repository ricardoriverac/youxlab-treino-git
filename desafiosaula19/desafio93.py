from time import sleep
print('-='*20)
print('\033[36mCADASTRO \033[32mDE JOGADOR\033[m \033[33mDE FUTEBOL\033[m')
print('-='*20)

jogador = {}
lista = []
soma = 0
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Quantas partidas você jogou?: '))
for c in range(0,jogador['partidas']):
    gol = int(input(f'Quantos gols você fez na partida {c+1}?: '))
    soma+=gol
    lista.append(gol)
    jogador['gol'] = lista
    jogador['total'] = soma
print('-='*20)
for k, v in jogador.items():
    print(f'O campo \033[1;35m{k}\033[m tem o valor {v} ')
    sleep(1)
print('-='*20)
sleep(1)
partida = jogador['partidas']
nome = jogador['nome']
print('O \033[36mjogador {}\033[m jogou \033[34m{} partidas\033[m'.format(nome, partida))
for i, v in enumerate(jogador['gol']):
    print(f'   → Na partida {i}, fez {v} gols ')
    sleep(1)
print(f'Foram um total de \033[1;36m{soma} GOLS!\033[m ')



    

