from time import sleep

jogadores = []

while True:
    jogador = dict()
    gols = []

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for jogo in range(1, partidas + 1):
        gol = int(input(f'Quantos gols {jogador["nome"]} fez na {jogo}° partida? '))
        gols.append(gol)

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:
        resposta = str(input('Quer colocar mais um jogador? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Digite direito!!')

    if resposta == 'N':
        break

print('-' * 40)
print('cod  nome               gols            total')
print('-' *40)
for i, j in enumerate(jogadores):
    print(f'{i:<4} {j["nome"]:<15} {str(j["gols"]):<20} {j["total"]}')
print('-' * 40)
while True:
    escolha = int(input('Mostrar dados de qual jogador? (Digite o código ou -1 para sair): '))
    if escolha == -1:
        break
    if escolha >= len(jogadores):
        print('Código inválido!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"].upper()} --')
        for i, g in enumerate(jogadores[escolha]['gols']):
            print(f'No {i+1}° jogo, {jogador["nome"]} fez {g} gols')
        print('-' * 40)
