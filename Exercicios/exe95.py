#Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualizações
#de detalhes do aproveitamento de cada jogador.

caixaDeIfo = dict()
time = list()
somaDosGols = 0

while True: 
    caixaDeIfo.clear()
    caixaDeGols = list()
    caixaDeIfo["cartaoAmarelo"] = 0
    caixaDeIfo["cartaoVermelho"] = 0

    caixaDeIfo["nome"] = input("\nDigite o nome do jogador: ")
    caixaDeIfo["partidas"] = int(input("Digite a quantidade de partidas jogadas: "))

    for g in range(caixaDeIfo["partidas"]):
        gols = int(input(f"\nQuantos gols você fez a partida {g+1}?: "))
        caixaDeGols.append(gols)
        
    caixaDeIfo["golsNasPartidas"] = caixaDeGols

    for toGols in caixaDeGols:
        somaDosGols += toGols
    
    tomouCartao = input("Tomou cartão? [S/N] ").strip().upper()

    if tomouCartao == "S":
        qualCartao = input("\nQual cartão você tomou? [Vermelho/Amarelo] ").strip().upper()
        quantCartao = int(input(f"Quantos cartoes {qualCartao}, você tomou? "))
        if qualCartao == "VERMELHO":
            caixaDeIfo["cartaoVermelho"] = quantCartao
        elif qualCartao == "AMARELO":
            caixaDeIfo["cartaoAmarelo"] = quantCartao
    
    time.append(caixaDeIfo.copy())
    pergunta = input("Você deseja continuar cadastrando? [S/N] ").strip().upper()

    if pergunta == "N":
        print("\nPrograma encerrado.\n")
        break

    if pergunta not in ["S", "N"]:
        print("\nResposta inválida.")
        print("Programa encerrado.\n")
        break

print(f"{'cod':<5}{'nome':<15}{'partidas':<12}{'golsNasPartidas':<20}{'cartaoAmarelo':<15}{'cartaoVermelho'}")
print("-" * 80)

for k, v in enumerate(time):
    print(f"{k:<5}", end='')
    print(f"{v['nome']:<15}", end='')
    print(f"{v['partidas']:<12}", end='')
    print(f"{str(v['golsNasPartidas']):<20}", end='')
    print(f"{str(v['cartaoAmarelo']):<15}", end='')
    print(f"{str(v['cartaoVermelho'])}")
print("-" * 80)

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
        jogador = time[busca]
        print(f"\n-- Dados do jogador {jogador['nome']}:")
    
        for i, g in enumerate(jogador["golsNasPartidas"]):
            print(f"  No jogo {i+1}, {jogador['nome']} fez {g} gols.")

        print(f"  Cartões amarelos: {jogador['cartaoAmarelo']}")
        print(f"  Cartões vermelhos: {jogador['cartaoVermelho']}")
        print("-" * 40)

print("Volte sempre.")