time = list()
jogador = dict()
gols = list()

while True:
    jogador["nome"] = str(input("Informe o nome do Jogador! "))
    jogador["partidas"] = int(input("Informe o numero de partidas! "))
    
    for c in range(0, jogador["partidas"]):
        gols.append(int(input("Quantos gols {} fez na partida {}? ".format(jogador["nome"], c))))
    
    jogador["gols"] = gols[:]
    jogador['totgols'] = sum(gols)
    gols.clear()

    time.append(jogador.copy())

    flag = str(input("Deseja continuar? S/N ")).strip().upper()[0]
    while flag not in "SN":
        flag = str(input("INVALIDO! Deseja continuar? S/N ")).strip().upper()[0]

    if flag == 'N':
        break

print("="*50)
print("COD Nome            Gols               Total")
for i, v in enumerate(time):
    print("{: >3} {: <16}{: <18} {: >5}".format(i, v["nome"], str(v["gols"]), v["totgols"]))
print("="*50)

while True:
    flag = int(input("Mostrar dados de quel Jogador? (999 Para!) "))
    while flag >= len(time):
        if flag == 999:
            break
        flag = int(input("Jogador INVALIDO! (999 Para!) "))

    if flag == 999:
        break
    else:
        print("{:-^50}".format("Levantamento do Jogador {}".format(time[flag]["nome"])))
        for c, v in enumerate(time[flag]["gols"]):
            print("No jogo {} {} fez {} gols!".format(c, time[flag]["nome"], v))