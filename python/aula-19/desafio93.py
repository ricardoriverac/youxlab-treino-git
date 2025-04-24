dados= dict()
dados['Jogador'] = str(input('Digite o nome do jogador:'))
dados['Jogos'] = int(input('informe a quantidade de jogos:'))
j = dados['Jogos']
gols = []
somagol = 0
for c in range(1,j+1):
    gols.append(int(input('Quantos gols no {}º jogo: '.format(c))))
    somagol = somagol + gols[c-1]
dados['Total de gols'] = somagol
dados['gols marcados'] =(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print('O campo {} tem o valor {}'.format(k,v))
print('-='*30)
print('O jogador {} participou de {} partidas:'.format(dados['Jogador'], dados['Jogos']))
for c in range(1,j+1):
    print('->> Na partida {}, fez {} gol(s)'.format(c, gols[c-1]))
