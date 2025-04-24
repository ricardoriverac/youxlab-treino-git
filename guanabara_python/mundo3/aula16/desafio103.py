def ficha(nome='', gols=''):
    if not nome:
        nome = '<desconhecido>'

    if str(gols).isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f'O jogador \033[34m{nome}\033[0m fez \033[32m{gols}\33[0m gol(s) no campeonato.')

# Programa principal
nome = str(input('Nome do jogador: '))
gols = input('Número de gols: ')

ficha(nome, gols)