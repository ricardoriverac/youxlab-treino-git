time=list()
jogador= dict()
partida=list()

while True:
    jogador.clear()
    jogador['nome'] = str (input('Nome: '))
    tot =int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in  range (0 , tot):
        partida.append(int(input(f' Quantos  gols  na partida {c}? ')))
    jogador['gols'] = partida[:]
    jogador['total']=sum(partida)
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO , S OU N')
    if resp == 'N':
        break 
for k , v  in enumerate(time):
    print(f'{k:>3}', end='')
    for d  in v.values():
        print(f'{str(d):<15}', end='')
    print()
