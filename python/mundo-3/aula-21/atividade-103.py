def ficha(nome='<desconhecido>', gols=0):
    """
    Exibe a ficha de um jogador com nome e número de gols.
    Parâmetros:
    nome -- nome do jogador (padrão: '<desconhecido>')
    gols -- número de gols (padrão: 0)
    """
    print(f"O jogador {nome} fez {gols} gol(s).")

n = input("Nome do jogador: ").strip()
g = input("Número de gols: ").strip()
n = n if n else '<desconhecido>'
g = int(g) if g.isdigit() else 0

ficha(n, g)
