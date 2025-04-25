listaDeJogadores = []
while True:
    jogador = {}
    listaDePartidas = []
    jogador['nome'] = input('Nome do jogador: ')
    numeroDePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for contador in range(numeroDePartidas):
        gols = int(input(f'Quantos gols {jogador["nome"]} fez na {contador + 1}ª partida? '))
        listaDePartidas.append(gols)
    jogador['gols'] = listaDePartidas[:]
    jogador['total'] = 0
    for quantidadeDeGols in listaDePartidas:
        jogador['total'] += quantidadeDeGols
    listaDeJogadores += [jogador]
    resposta = input('Deseja continuar? (S/N) ').strip().upper()
    while resposta not in ['S', 'N']:
        resposta = input('ERRO! Responda apenas S ou N: ').strip().upper()
    if resposta == 'N':
        break
print('\n' + '\033[35m-\033[m'*40)
print(f'{"codigo":<8}{"nome":<20}{"total de gols":<15}')
print('\n' + '\033[35m-\033[m'*40)
indice = 0
while indice < len(listaDeJogadores):
    print(f'{indice:<8}{listaDeJogadores[indice]["nome"]:<20}{listaDeJogadores[indice]["total"]:<15}')
    indice += 1
print('\n' + '\033[35m-\033[m'*40)
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if codigo == 999:
        break
    if codigo < 0 or codigo >= len(listaDeJogadores):
        print(f'ERRO! Não existe jogador com código {codigo}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {listaDeJogadores[codigo]["nome"]} --')
        partida = 0
        while partida < len(listaDeJogadores[codigo]['gols']):
            print(f'  No jogo {partida + 1} fez {listaDeJogadores[codigo]["gols"][partida]} gol(s).')
            partida += 1
print('\n' + '\033[35m-\033[m'*40)
print ('-=' * 4, f'\033[35m« VOLTE SEMPRE »\033[m','-=' * 4 )

