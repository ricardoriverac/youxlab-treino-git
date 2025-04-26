def ficha(jogador='DESCONHECIDO', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) ')
    
nome = input('Nome do jogador: ')
gols = input('Quantos gols você fez?: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
    
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)







def ficha(jogador='DESCONHECIDO', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) ')
    
    
nome = input('Nome: ')
gols = input('Quantos gols fez?: ')

if gols.isnumeric():
    int(gols)
else:
    gols = 0
    
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)