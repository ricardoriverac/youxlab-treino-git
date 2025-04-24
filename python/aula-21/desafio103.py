def ficha(n, g=0):
    g = 0
    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato'
    elif gols == '':
        return f'O jogador {n} fez {g} gol(s) no campeonato'
    else:
        return f'O jogador {n} fez {gols} gol(s) no campeonato'
nome = str(input('Nome do jogador: '))
gols = str(input('Números de gols: '))
print(ficha(nome, gols))