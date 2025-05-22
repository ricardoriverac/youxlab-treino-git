time = []
jogador = {}
gols = []
while True:
    jogador['Nome'] = str(input('Nome: '))
    Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    for i in range(Partidas):
            gols.append(int(input(f'Quantos gols na partida {i + 1}?')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S / N]')).upper()
        if resp not in 'SN':
            print("ERRO, escreva somente S ou N")
        else:
            break
    if resp == 'N':
        break
    jogador.clear()
    gols.clear()
print('Cod nome      gols             total')
for i in range(len(time)):
    print(f'{i} {(time[i])["Nome"]}   {(time[i])["Gols"]}   {(time[i])["Total"]}')
while True:
    escolha = int(input(f'Mostrar dados de qual jogador? [999 para parar] '))
    if escolha == 999:
        break
    print(f'LEVANTAMENTO do jogador {(time[escolha])["Nome"]}')
    for i in range(len((time[escolha])["Gols"])):
        print(f'No jogo {i} fez {time[escolha]["Gols"][i]} gols')
