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
     {"nome": "Mauricio", "gols": 6, "nacionalidade": "ES"}
]

#gols por nacionalidade
gols_por_nacionalidade = {}

for jogador in jogadores:
    nacionalidade = jogador["nacionalidade"]
    if nacionalidade not in gols_por_nacionalidade:
        gols_por_nacionalidade[nacionalidade] = []
    gols_por_nacionalidade[nacionalidade].append(jogador["gols"])

#média
media_por_nacionalidade = {}
for nacionalidade, lista_gols in gols_por_nacionalidade.items():
    media = sum(lista_gols) / len(lista_gols)
    media_por_nacionalidade[nacionalidade] = media

#resultado
for nacionalidade, media in media_por_nacionalidade.items():
    print(f"{nacionalidade}: média de {media:.2f} gols")