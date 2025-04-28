jogador= dict()
partida=list()
jogador['nome'] = str (input('Nome: '))
tot =int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in  range (0 , tot):
    partida.append(int(input(f' Quantos  gols  na partida {c}? ')))
jogador['gols'] = partida[:]
jogador['total']=sum(partida)
print('='* 15)
print(jogador)
print('='* 15)
for k ,  v in  jogador.items():
    print(f' O campo {k} tem o valor  {v}')
print(f' O jogador {jogador["nome"]} jogou  {len(jogador["gols"])} partidas ')
for i ,  v in  enumerate(jogador['gols']):
    print(f' >>Na partida  {i} , fez  {v} gols')
print(f'Foi um total  de {jogador["total"]} gols')
