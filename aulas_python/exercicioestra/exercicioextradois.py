from time import sleep
print('-='*20)
print('RANK  JOGADORES')
print('-='*20)
somaBrasil = somaJapao = somaUsa = somaFranca =  somaArgentina = 0
mediaBrasil = mediaUsa = mediaJapao = mediaFranca = mediaArgentina =0
contagem = contagemUsa = contagemJapao = contagemfranca = contagemArgentina = 0
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
for c in range(0, len(jogadores)):
    if jogadores[c]['nacionalidade'] in 'BR':
        contagem +=1
        somaBrasil += jogadores[c]['gols']
    if jogadores[c]['nacionalidade'] in 'USA':
        contagemUsa+= 1
        somaUsa += jogadores[c]['gols']
    if jogadores[c]['nacionalidade'] in 'JP':
        contagemJapao += 1
        somaJapao += jogadores [c]['gols']
    if jogadores[c]['nacionalidade'] in 'FR':
        contagemfranca += 1
        somaFranca += jogadores[c]['gols']
    if jogadores[c]['nacionalidade'] in 'AR':
        contagemArgentina += 1
        somaArgentina += jogadores[c]['gols']
        
mediaBrasil = somaBrasil/contagem
mediaUsa = somaUsa/contagemUsa
mediaJapao = somaJapao/contagemJapao
mediaFranca = somaFranca/contagemfranca
mediaArgentina = somaArgentina/contagemArgentina

print(f'A média dos gols da \033[33mNacionalidade BR\033[m é {mediaBrasil:.2f}')
print(f'A média dos gols da \033[32mNacionalidade USA\033[m é {mediaUsa:.2f}')
print(f'A média dos gols da \033[31mNacionalidade JP\033[m é {mediaJapao:.2f}')  
print(f'A média dos gols da \033[36mNacionalidade FR\033[m é {mediaBrasil:.2f}')
print(f'A média dos gols da \033[35mNacionalidade AR\033[m é {mediaArgentina:.2f}')

# golPais = {}
# contadorPais = {}
# for jogador in jogadores:
#     pais = jogador['nacionalidade']
#     golPais = jogador['gols']
#     contadorPais += 1
    
ranking = []
print('-='*20)
print('\033[1;35mRANKING DA MÉDIA DOS GOLS DE CADA PAÌS\033[m')
print('-='*20)
ranking.append(mediaBrasil)
ranking.append(mediaArgentina)
ranking.append(mediaFranca)
ranking.append(mediaJapao)
ranking.append(mediaUsa)
ranking.sort(reverse=True)
for i, v in enumerate(ranking):
        print(f'Em {i+1}º lugar: ', end='')
        print(f'{v:.2f}')
print('-='*20)
