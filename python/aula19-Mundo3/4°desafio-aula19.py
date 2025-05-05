#CADASTRO DE JOGADOR DE FUTEBOL 
jogador={}
partidas=[]
jogador['nome']=str(input('Nome:'))
totalPartidas=int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
for contador in range(0, totalPartidas):
    partidas.append(int(input(f'    Quantos gols na {contador+1}° partida?: ')))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print()
print('RESULTADOS:')
print(jogador)
print()
for key, value in jogador.items():
    print(f'O chave {key} tem o valor {value}')
print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for indice, value in enumerate(jogador['gols']):
    print(f'--> Na {indice+1}° partida, fez {value} gols')
print(f'Ao todo foram {jogador["total"]} em {totalPartidas}')