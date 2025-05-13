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
    {"nome": "Mauricio", "gols": 6, "nacionalidade": "AR"}
]

golsPorPais = {}
jogadoresPorPais = {}

for jogador in jogadores:
    pais = jogador['nacionalidade']
    gols = jogador['gols']

    if pais not in golsPorPais:
        golsPorPais[pais] = 0
        jogadoresPorPais[pais] = 0

    golsPorPais[pais] += gols
    jogadoresPorPais[pais] += 1

print('Média de gols por país:')
for pais in golsPorPais:
    media = golsPorPais[pais] / jogadoresPorPais[pais]
    print(f"{pais}: {media:.2f}")
print()




golsPorPais = {}
jogadoresPorPais = {}

for jogador in jogadores:
    pais = jogador["nacionalidade"]
    gols = jogador["gols"]

    if pais not in golsPorPais:
        golsPorPais[pais] = 0
        jogadoresPorPais[pais] = 0

    golsPorPais[pais] += gols
    jogadoresPorPais[pais] += 1

mediaPorPais = {}

for pais in golsPorPais:
    media = golsPorPais[pais] / jogadoresPorPais[pais]
    mediaPorPais[pais] = media

ranking = sorted(mediaPorPais.items(), key=lambda item: item[1], reverse=True)

print("Ranking de médias de gols por países:")
for posicao, (pais, media) in enumerate(ranking, start=1):
    print(f"{posicao}° lugar - {pais}: {media:.2f}")