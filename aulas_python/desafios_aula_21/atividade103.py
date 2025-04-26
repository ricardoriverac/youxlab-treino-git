def t103(jogador='', gols=0):
    if jogador.strip() == '':
        jogador = '<desconhecido>'
        
    try:
        gols = int(gols)
    except (ValueError, TypeError):
        gols = 0 
        
    if jogador == '<desconhecido>' and gols == 0:
        print('Nenhum dado fornecido')
    else:
        print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

player = str(input('Qual o nome do jogador?: '))
goleada = input('Quantos gols ele fez?: ')
t103(player, goleada)