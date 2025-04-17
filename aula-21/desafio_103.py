def jogo():
    print('-' * 30)
    nome = str(input('Nome do Jogador: ')).strip()
    if nome == '':
        nome = "<desconhecido>"
    gols = str(input('Número de Gols: ')).strip()
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    resultado = f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    return resultado

print(jogo())
