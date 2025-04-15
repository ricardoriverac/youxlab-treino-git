time = []

while True:
    jogador = {}
    gols = []

    jogador['nome'] = input("Nome do jogador: ")
    num_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range(num_partidas):
        gol = int(input(f"  Quantos gols na partida {i + 1}? "))
        gols.append(gol)

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())

    continuar = input("Deseja adicionar outro jogador? [S/N] ").strip().upper()
    if continuar != 'S':
        break

print("\n{:<5} {:<15} {:<20} {:<5}".format("Cod", "Nome", "Gols", "Total"))
print("-" * 50)
for i, j in enumerate(time):
    print(f"{i:<5} {j['nome']:<15} {str(j['gols']):<20} {j['total']:<5}")

while True:
    busca = input("\nDigite o código do jogador para ver detalhes (999 para sair): ")
    if not busca.isdigit():
        print("Por favor, digite um número válido.")
        continue
    busca = int(busca)

    if busca == 999:
        print("Encerrando o programa.")
        break

    if busca < 0 or busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}.")
    else:
        jogador = time[busca]
        print(f"\n==> Levantamento do jogador {jogador['nome']}:")
        for i, g in enumerate(jogador['gols']):
            print(f"   No jogo {i + 1} fez {g} gol(s)")
