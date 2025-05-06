soma_gols = 0
contagem = 0

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

# for jogador in jogadores:
#     print(jogador['nacionalidade'])
#     print(jogador['gols'])
#     nacionalidade = jogador["nacionalidade"]
#     soma_gols = nacionalidade =+ jogador['gols']
#     contagem[nacionalidade] += 1

br = []
ar = []
jp = []
usa = []
fr = []
total = []

soma = 0
somaAG = 0
somaJP = 0
somaUSA = 0
somaFR = 0

for i in jogadores:
    if i['nacionalidade'] == 'BR':
        br.append(i['gols'])


for i in br:
    soma += i
    mediaBR = soma/len(br)
total.append(mediaBR)

for i in jogadores:
    if i['nacionalidade'] == 'AR':
        ar.append(i['gols'])


for i in ar:
    somaAG += i
    mediaAG = somaAG/len(ar)
total.append(mediaAG)

for i in jogadores:
    if i["nacionalidade"] == 'USA':
        usa.append(i['gols'])

for i in usa:
    somaUSA += i
    mediaUSA = somaUSA/len(usa)
total.append(mediaUSA)

for i in jogadores:
    if i['nacionalidade'] == 'FR':
        fr.append(i['gols'])
        
for i in fr:
    somaFR += i
    mediaFR = soma/len(fr)
total.append(mediaFR)

for i in jogadores:
    if i['nacionalidade'] == 'JP':
        jp.append(i['gols'])

for i in jp:
    somaJP += i
    mediaJP = soma/len(jp)
total.append(mediaJP)





print('=='*20)
print(f'A média da França é {mediaFR:.2f}')
print('=='*20)
print(f'A média do EUA é {mediaUSA:.2f}')
print('=='*20)
print(f'A média da Argentina é {mediaAG:.2f}' )
print('=='*20)
print(f'A média do Brasil é {mediaBR:.2f} ')
print('=='*20)
print(f'A média do Japão é {mediaJP :.2f}')
print('=='*20)

print('             Rank das Médias das Seleçoes')
print('=='*20)



print(f'A frança tem a maior Média {total[3]}')
print('=-'*20)
print(f'O Japão tem a segunda maior Média {total[4]}')
print('=-'*20)
print(f'O Brasil tem a Terceira maior Média {total[0]}')
print('=-'*20)
print(f'A Argentina tem a quarta maior Média {total[1]}')
print('=-'*20)
print(f'O USA tem a Qquinta maior Média {total[2]}')
print('=-'*20)














   

        

        

        

