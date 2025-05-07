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
    {"nome": "Mauricio", "gols": 5, "nacionalidade": "HO"},
    {"nome": "Mauricio", "gols": 10, "nacionalidade": "HO"},
    {"nome": "Mauricio", "gols": 15, "nacionalidade": "HO"},
]
gols_por_nacionalidade = {}
jogadores_por_nacionalidade = {}
ranking = []
for jogador in jogadores:
    nacionalidade = jogador["nacionalidade"]
    gols = jogador["gols"]
    if nacionalidade in gols_por_nacionalidade:
        gols_por_nacionalidade[nacionalidade] += gols
        jogadores_por_nacionalidade[nacionalidade] += 1
    else:
        gols_por_nacionalidade[nacionalidade] = gols
        jogadores_por_nacionalidade[nacionalidade] = 1
print(gols_por_nacionalidade)
print(jogadores_por_nacionalidade)
print("média de gols por nacionalidade:")
for nacionalidade in gols_por_nacionalidade:
    total_gols = gols_por_nacionalidade[nacionalidade]
    total_jogadores = jogadores_por_nacionalidade[nacionalidade]
    media = total_gols / total_jogadores
    print(f'{nacionalidade}: {media:.2f}')
lista_dos_gols = gols_por_nacionalidade
print(lista_dos_gols)
ranking.append((nacionalidade, media))
for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)): 
        if ranking[j][1] > ranking[i][1]:
            ranking[i], ranking [j] = ranking[j], ranking[i]
            print('Ranking de nacionalidade por média (de maior pra menor.) ')
for posicao, (nacionalidade, media) in enumerate(ranking, start=1):
    print(f'{posicao}, {nacionalidade} - Média : {media:.2f}')