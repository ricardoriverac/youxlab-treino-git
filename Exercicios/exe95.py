#Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualizações
#de detalhes do aproveitamento de cada jogador.

caixaDeIfo = dict()
time = list()
somaDosGols = 0

while True: 
    caixaDeIfo.clear()
    caixaDeGols = list()
    caixaDeIfo["nome"] = input("\nDigite o nome do jogador: ")
    caixaDeIfo["partidas"] = int(input("Digite a quantidade de partidas jogadas: "))

    for g in range(caixaDeIfo["partidas"]):
        gols = int(input(f"\nQuantos gols você fez a partida {g+1}?: "))
        caixaDeGols.append(gols)
        
    caixaDeIfo["golsNasPartidas"] = caixaDeGols
    time.append(caixaDeIfo.copy())

    for toGols in caixaDeGols:
        somaDosGols += toGols

    pergunta = input("Você deseja continuar cadastrando? [S/N] ").strip().upper()

    if pergunta == "N":
        print("\nPrograma encerrado.\n")
        break

    if pergunta not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Programa encerrado.\n")
        break

print("cod ", end='')
for i in caixaDeIfo.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 40)

for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-" * 40)

while True:
    busca = input("Você quer buscar os dados de qual jogador? [Digite: Parar, para encerrar.] ").strip().upper()

    if busca == "PARAR":
        print("\nBusca encerrada.")
        break

    if not busca.isdigit():
        print("Digite apenas o número do codigo do jogador.")
        continue

    busca = int(busca)

    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f"\n-- Dados do jogador {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]["golsNasPartidas"]):
            print(f"  No jogo {i+1}, {time[busca]['nome']} fez {g} gols.")
        print("-" * 40)
print("Volte sempre.")