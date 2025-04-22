nome = str(input('Nome do jogador: '))
gols = int(input('Gols do jogador: '))
def lin():
    print('--'*20)


def ficha(nome,gols):
    lin()
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato. ')


ficha(nome,gols)