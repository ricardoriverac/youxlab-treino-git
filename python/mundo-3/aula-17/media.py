from collections import defaultdict

# Agrupar os gols por nacionalidade
gols_por_nacionalidade = defaultdict(list)

for jogador in jogadores:
    gols_por_nacionalidade[jogador["nacionalidade"]].append(jogador["gols"])

# Calcular a média
media_por_nacionalidade = {
    nacionalidade: sum(gols) / len(gols)
    for nacionalidade, gols in gols_por_nacionalidade.items()
}

# Exibir o resultado
for nacionalidade, media in media_por_nacionalidade.items():
    print(f"{nacionalidade}: média de {media:.2f} gols")
