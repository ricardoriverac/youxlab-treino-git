def media(lista):
    soma = 0
    cont = 0
    for b in lista:
        cont += 1
        soma += b['gols']
    media = soma / cont
    return media


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
    {"nome": "CARLOS", "gols": 2, "nacionalidade": "UK"},
    {"nome": "LUCAS", "gols": 4, "nacionalidade": "UK"},
    {"nome": "LUCAS", "gols": 5, "nacionalidade": "UKA"}
]

paises = []

for n in jogadores:
    if n["nacionalidade"] not in paises:
        paises.append(n["nacionalidade"])

for pais in paises:
    jogadoresDoPais = []
    for j in jogadores:
        if j["nacionalidade"] == pais:
            jogadoresDoPais.append(j)
    media2 = media(jogadoresDoPais)
    print(f'{pais} ➤ Média de gols: {media2:.2f}')

#PRIMEIRA TENTATIVA
# lista_ordenada = sorted(media2, key=lambda item: item[1], reverse=True)
# print(lista_ordenada)

gols_por_pais = {}

for jogador in jogadores:
    pais = jogador['nacionalidade']
    gols = jogador['gols']
    if pais in gols_por_pais:
        gols_por_pais[pais] += gols
    else:
        gols_por_pais[pais] = gols
        
    ranking = sorted(gols_por_pais.items(), key=lambda x: x[1], reverse=True)

print("\n-=-=-=-=-=-=-=-==Ranking=-=-=-=-=-=-=-=-=-")
for posicao, (pais, total_gols) in enumerate(ranking, start=1):
    print(f"{posicao}. {pais} ➤ {total_gols} gols")