dic = {}
time = []
gols = []
totalGols = cont = 0

while True:
    dic.clear()
    print('-='*30)
    dic["nome"] = str(input('Nome do jogador: '))
    dic["partidas"]= int(input('Partidas: '))

    gols.clear()

    for c in range(dic["partidas"]):
        g = int(input(f'Quantos gols ele fez na partida {c + 1}? '))
        gols.append(g)

    
    dic["gols"] = gols[:]
    dic["total"] = sum(gols)
    cont += 1
    time.append(dic.copy())

    continuar = str(input('Deseja continuar? [s/n]')).lower()[0]

    if continuar == 'n':
        break
print("\n" + "-" * 40)
print("cod nome     gols       total de gols")
print("-" * 40)
for i, jogador in enumerate(time):
    nome = jogador['nome'].ljust(9)
    gols_str = str(jogador['gols']).ljust(11)
    print(f"{i:<3} {nome} {gols_str} {jogador['total']}")
print("-" * 40)

while True:
    resp = input("\nDeseja mostrar dados detalhados de qual jogador? (Digite 999 para sair.) ")
    if resp == '999':
        break
    elif resp.isdigit() and int(resp) < len(time):
        idx = int(resp)
        jogador = time[idx]
        print(f"\n Detalhes do jogador {jogador['nome']}:")
        for i, g in enumerate(jogador['gols']):
            print(f"   No jogo {i + 1} fez {g} gols.")
    else:
        print("Código inválido. Tente novamente.")