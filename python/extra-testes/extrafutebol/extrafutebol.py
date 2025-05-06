from defs import *

jogadores = [
    {
        "nome": "Ricardo",
        "gols": 5,
        "nacionalidade": "BR"
    },
    {
        "nome": "Walter",
        "gols": 7,
        "nacionalidade": "BR"
    },
    {
        "nome": "Japa",
        "gols": 12,
        "nacionalidade": "JP"
    },
    {
        "nome": "Joao",
        "gols": 9,
        "nacionalidade": "JP"
    },
    {
        "nome": "Augusto",
        "gols": 2,
        "nacionalidade": "USA"
    },
    {
        "nome": "Cesar",
        "gols": 5,
        "nacionalidade": "USA"
    },
    {
        "nome": "Kaio",
        "gols": 2,
        "nacionalidade": "JP"
    },
    {
        "nome": "MESSI",
        "gols": 20,
        "nacionalidade": "AR"
    },
    {
        "nome" : "Cristiano",
        "gols" : 3,
        "nacionalidade" : "PT"
    }
]

soma = 0
paises = []

rank = {}

for n in jogadores:
    if n["nacionalidade"] not in paises:
        paises.append(n["nacionalidade"])

titulo('Média de Gols das seleções')
quebraDeLinha()

for pais in paises:
    jogadoresDoPais = []
    cont = 0
    for j in jogadores:
        if j["nacionalidade"] == pais:
            jogadoresDoPais.append(j)
    soma = 0

    for k in jogadoresDoPais:
        soma += k["gols"]
        calculoMedio = soma / len(jogadoresDoPais)

    print(f'{pais} -> Média de gols: {calculoMedio}')
    rank[(pais)] = calculoMedio

quebraDeLinha()
titulo('Ranking de maior média de Gols')

rankeamento = sorted(rank.items(), key=valor, reverse=True)
for k,v in rankeamento:
    print(f'{cont+1}º Lugar  -> {k}: Média -> {v}')
    cont += 1

# Feito sem dinâmica

# mediaBr = mediaJp = mediaEua = 0
# jogadoresJapao = []
# jogadoresBr = []
# jogadoresUsa = []
# for j in jogadores:
#     if j["nacionalidade"] == "JP":
#         jogadoresJapao.append(j)
#     elif j["nacionalidade"] == "BR":
#         jogadoresBr.append(j)
#     elif j["nacionalidade"] == "USA":
#         jogadoresUsa.append(j)

# for gols in jogadoresBr:
#     soma += gols["gols"]
# mediaBr = soma / len(jogadoresBr)
# soma = 0

# for gols in jogadoresJapao:
#     soma += gols["gols"]
# mediaJp = soma / len(jogadoresJapao)
# soma = 0

# for gols in jogadoresUsa:
#     soma += gols["gols"]
# mediaEua = soma / len(jogadoresUsa)
# soma = 0

# for gols in jogadoresUsa:
#     soma += gols["gols"]
# mediaEua = soma / len(jogadoresUsa)
# soma = 0


# print(paises)
# print(f'A média de gols do Brasil é de {mediaBr}')
# print(f'A média de gols do Japão é de {mediaJp}')
# print(f'A média de gols dos EUA é de {mediaEua}')