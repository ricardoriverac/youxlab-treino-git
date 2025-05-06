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

golsPorNacionalidade = {}
for jogador in jogadores:
    nacionalidade = jogador["nacionalidade"]
    if nacionalidade not in golsPorNacionalidade:
        golsPorNacionalidade[nacionalidade] = []
    golsPorNacionalidade[nacionalidade].append(jogador["gols"])
mediaPorNacionalidade = {}
for nac, listaGols in golsPorNacionalidade.items():
    media = sum(listaGols) / len(listaGols)
    mediaPorNacionalidade[nac] = media
print ('-=' * 4, f'\033[35mMÉDIA POR NACIONALIDADE\033[m','-=' * 4 )
for nac, media in mediaPorNacionalidade.items():
    print(f"{nac}: média de {media:.2f} gols")