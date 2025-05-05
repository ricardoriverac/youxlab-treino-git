jogador = {}
jogador['nome'] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
gols = []
for i in range(partidas):
    gols.append(int(input(f"Quantos gols na partida {i + 1}? ")))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print("Aproveitamento do jogador:")
for chave, valor in jogador.items():
    print(f"{chave.capitalize()}: {valor}")
print("Detalhamento:")
for i, g in enumerate(jogador['gols']):
    print(f"  => Na partida {i + 1}, fez {g} gol(s).")

print(f"Total de gols no campeonato: {jogador['total']}")