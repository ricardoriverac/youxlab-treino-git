import unicodedata

def remover_acentos(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
times = ('Palmeiras',"Flamengo","Fluminense",
"Bragantino","Ceara","Corinthians","Cruzeiro",
"Vasco","Juventude","São Paulo","Mirassol",
"Internacional","Bahia","Fortaleza","Bota Fogo",
"Vitoria","Atletico-MG","Santos","Gremio","Sport")
print("============"*8)
print(times)
print("============"*8)
print(f"0s cincos primeiros da tabela sao{times[0:5]}")
print("============"*8)
print(f"Times em ordem alfabetica{sorted(times)}")
print("============"*8)
while True:
    opçao = str(input("Deseja ver quem esta na zona de rebaixamento? [S/N]: ")).upper().strip()
    if opçao != "S" and opçao != "N":
        print("Erro tente novamente")
    elif opçao == "S":
        print("============"*8)
        print(f"Quem esta na zona🅱️:{times[16:]} ")
        print("============"*8)
        break
    else:
        break
times_normalizados = [remover_acentos(time).lower() for time in times]

while True:
    timeop = input("Digite algum time para saber sua classificação: ").strip()
    timeop_normalizado = remover_acentos(timeop).lower()

    if timeop_normalizado in times_normalizados:
        posicao = times_normalizados.index(timeop_normalizado) + 1
        time_real = times[posicao - 1]
        print(f"Time encontrado: {time_real}")
        print(f'Posição na classificação: {posicao}º lugar')
        break
    else:
        print("Time não encontrado na classificação. Tente novamente.")