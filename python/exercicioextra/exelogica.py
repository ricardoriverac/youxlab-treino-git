paises = []
jogadores = [
    {"nome": "Ricardo", "gols": 5, "nacionalidade": "BR"},
    {"nome": "Walter", "gols": 7, "nacionalidade": "BR"},
    {"nome": "Japa", "gols": 12, "nacionalidade": "JP"},
    {"nome": "Joao", "gols": 9, "nacionalidade": "JP"},
    {"nome": "Augusto", "gols": 2, "nacionalidade": "USA"},
    {"nome": "Cesar", "gols": 5, "nacionalidade": "USA"},
    {"nome": "Kaio", "gols": 2, "nacionalidade": "JP"},
    {"nome": "Lucas", "gols": 4, "nacionalidade": "BR"},
    {"nome": "Felipe", "gols": 8, "nacionalidade": "BR"},
    {"nome": "Takeshi", "gols": 6, "nacionalidade": "JP"},
    {"nome": "Yuki", "gols": 10, "nacionalidade": "JP"},
    {"nome": "Max", "gols": 3, "nacionalidade": "USA"},
    {"nome": "Julien", "gols": 7, "nacionalidade": "FR"},
    {"nome": "Pierre", "gols": 5, "nacionalidade": "FR"},
    {"nome": "Emiliano", "gols": 2, "nacionalidade": "AR"},
    {"nome": "Ricardo Jr.", "gols": 9, "nacionalidade": "BR"},
    {"nome": "Santos", "gols": 1, "nacionalidade": "BR"},
    {"nome": "Gabriel", "gols": 3, "nacionalidade": "USA"},
    {"nome": "Mauricio", "gols": 6, "nacionalidade": "AR"},
    {"nome": "Fabricio", "gols": 1, "nacionalidade": "ES"},
    {"nome": "paulo", "gols": 4, "nacionalidade": "ES"}

]
rank = {}
colocando_na_lista = []
for jogador in jogadores:
    if jogador['nacionalidade'] not in paises:
        paises.append(jogador["nacionalidade"])

for pais in paises:
    jogadorpais = []
    for na in jogadores:
        if na["nacionalidade"] == pais:
            jogadorpais.append(na)
    soma = 0

    for gol in jogadorpais:
        soma += gol["gols"]
        calculamedia = soma / len(jogadorpais)
    print(f'{pais} a média desse país é {calculamedia}')
    colocando_na_lista.append(calculamedia)
    rank[pais] = calculamedia
ranking = sorted(rank.items() , key=lambda x: x[1] , reverse=True)
for contandor , (pais,calculamedia) in enumerate(ranking):
    print(f'{contandor+1}° lugar {pais} com a média {calculamedia}')