def ficha(nome, gols):
    if not nome:

        nome = '<desconhecido>'

    if not gols:

        gols = 0

    return (f'O jogador {nome} fez {gols} gols')



n = str(input('Nome do jogador: '))

g = str(input('Gols: '))

print(ficha(n, g))