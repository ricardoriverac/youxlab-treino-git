def ficha():
    global nome
    global gols
    global camp
    nome = str(input('Qual o nome do Pé torto? '))
    gols = int(input('Quantos gols o jogador fez no campeonato? '))
    camp = str(input('Qual compeonato? '))

ficha()
print(f'O jogador {nome} fez {gols} no campeonato {camp}')
