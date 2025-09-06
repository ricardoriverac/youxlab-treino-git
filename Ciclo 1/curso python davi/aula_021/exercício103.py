def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} marcou {gols} gol(s) no campeonato.")
nome_jogador = input("Nome do jogador: ").strip()
gols_jogador = input("Número de gols: ").strip()
if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
ficha(nome_jogador if nome_jogador else '<desconhecido>', gols_jogador)