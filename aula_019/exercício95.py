time = []
while True:
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ").strip()
    total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    gols = []
    for i in range(total_partidas):
        gols.append(int(input(f"  Quantos gols na partida {i + 1}? ")))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    continuar = input("Deseja cadastrar outro jogador? [S/N] ").strip().upper()
    if continuar == 'N':
        break
print("TABELA DE JOGADORES:")
print(f"{'Cod':<4} {'Nome':<15} {'Gols':<20} {'Total':<5}")
print("=" * 50)
for i, jogador in enumerate(time):
    print(f"{i:<4} {jogador['nome']:<15} {str(jogador['gols']):<20} {jogador['total']:<5}")
print("=" * 50)
while True:
    busca = input("Mostrar dados de qual jogador? (Digite o código ou 's' para sair): ")
    if busca == 's':
        print("encerrando o programa...")
        break
    elif not busca.isdigit() or int(busca) >= len(time):
        print("Código inválido! Tente novamente.")
    else:
        codigo = int(busca)
        jogador = time[codigo]
        print(f"\n🔍 Detalhamento do jogador: {jogador['nome']}")
        for i, g in enumerate(jogador['gols']):
            print(f"  => No jogo {i + 1}, fez {g} gol(s).")
        print("=" * 50)