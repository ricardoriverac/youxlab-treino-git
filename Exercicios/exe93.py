#Crie um programa que gerencie o aproveitamento de um jogador de futebol
#O programa deve ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
#feitos em cada partida. No final, tudo isso será guardado em um discionario, incluindo o total de gols feitos durante o campeonato.

caixaDeIfo = dict()
caixaDeGols = list()
somaDosGols = 0

caixaDeIfo["nome"] = input("\nDigite o nome do jogador: ")
caixaDeIfo["partidas"] = int(input("Digite a quantidade de partidas jogadas:"))

for g in range(caixaDeIfo["partidas"]):
    gols = int(input(f"\nQuantos gols você fez a partida {g+1}?: "))
    caixaDeIfo["golsNasPartidas"] = caixaDeGols
    caixaDeGols.append(gols)

for toGols in caixaDeGols:
    somaDosGols += toGols

print(f"\nO Jogador {caixaDeIfo['nome']} jogou {caixaDeIfo['partidas']} partidas.")

for p in range(caixaDeIfo["partidas"]):
    print(f"Na partida {p+1}, fez {caixaDeGols[p]} gols.")
print(f"Foi um total de {somaDosGols} gols.\n")
    