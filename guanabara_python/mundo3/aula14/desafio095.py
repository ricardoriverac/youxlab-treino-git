import time

jogadores = []  # Lista de todos os jogadores
resp = 'S'

while resp.upper() != 'N':
    jogador = dict()
    gols_por_partida = []
    totalgols = 0

    jogador['nome'] = str(input('Digite o nome do jogador: ')).title().strip()
    numeropartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

    for partida in range(numeropartidas):
        gols = int(input(f'  Quantos gols na partida {partida + 1}?: '))
        gols_por_partida.append(gols)
        totalgols += gols

    jogador['gols'] = gols_por_partida[:]
    jogador['total'] = totalgols
    jogadores.append(jogador.copy())

    resp = str(input('Quer continuar cadastrando jogadores (S/N)?: '))
    while resp.upper() not in ('S', 'N'):
        resp = str(input('Digite S ou N: '))

# Exibir tabela resumo
print(30*'-')
print('\033[1;37mNº     Nome            Gols            Total\033[m')
print(30*'-')

for pos, jogador in enumerate(jogadores):
    print(f'{pos:<6}{jogador["nome"]:<15}{str(jogador["gols"]):<15}{jogador["total"]:<5}')
print(30*'-')

# Detalhar dados de jogadores
while True:
    resp = int(input('Deseja ver dados de qual jogador? \033[1;33m(999 interrompe): '))
    if resp == 999:
        print('\033[m')
        break
    if resp < 0 or resp >= len(jogadores):
        print(f'\033[1;31mOps... Tente novamente. Não há jogador com esse número.\033[m')
    else:
        print(f'\033[1;36m-- Detalhes do jogador {jogadores[resp]["nome"]}:\033[m')
        for i, g in enumerate(jogadores[resp]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
print('FINALIZANDO...')
time.sleep(1)
print('='*10, 'VOLTE SEMPRE', '='*10)
