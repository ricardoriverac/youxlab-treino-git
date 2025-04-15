jogador = {}

jogador['nome'] = input("Nome do jogador: ")

num_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

gols = []

for i in range(num_partidas):
    gol = int(input(f"Quantos gols na partida {i + 1}? "))
    gols.append(gol)

jogador['gols'] = gols
jogador['total'] = sum(gols)

print("\nDados do jogador:")
print(jogador)

print("\nDetalhamento:")
print(f"Nome do jogador: {jogador['nome']}")
print(f"Partidas jogadas: {num_partidas}")
for i, g in enumerate(jogador['gols']):
    print(f"  => Na partida {i + 1}, fez {g} gol(s)")
print(f"Total de gols: {jogador['total']}")
