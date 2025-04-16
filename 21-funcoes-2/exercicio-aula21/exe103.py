def ficha(nome,gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol == "":
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


#programa principal 
nome_do_jogador = str(input('Nome do jogador: '))
gols = str(input('Quantos gols marcou: '))
ficha(nome_do_jogador,gols)