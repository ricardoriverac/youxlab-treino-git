def ficha(nome='', gols=0):
    if nome == '':
        nome = 'desconhecido'
    if gols == True:
        gols = gol
    return print(f'O jogador {nome} marcou {gols} gols')

    
    

nome = str(input('Digite o nome do jogador: '))
gol = input('Quantos gols ele fez? ')
if gol == '':
    gol = 0
ficha(nome, gol)