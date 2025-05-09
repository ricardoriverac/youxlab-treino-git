paises = []
maiorMedia = []
contadorPaises = []
maiorMediaDicionario = []
maiorValor = []
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
#     if jogador['nacionalidade'] == "AR":
#         contadorBR += 1
#         somaBR += (jogador['gols'])
# print(somaBR)
# media = somaBR/contadorBR

# print(media)

#print(jogador['nacionalidade'])

for jogador in jogadores:

    if jogador['nacionalidade'] not in paises:
        paises.append(jogador['nacionalidade'])
print(paises)

for contadorPaises in paises:

    soma = 0
    contador = 0
    media = 0

    for jogador in jogadores:
        if jogador['nacionalidade'] == contadorPaises:

            contador += 1 
            soma += (jogador['gols'])

    media = soma/contador
    maiorMedia.append(media)
    print(f'{contadorPaises} possui a soma = {soma}')
    print(f'{contadorPaises} possui a média = {media}')

for valor in maiorMedia:
    if valor > maiorValor:
        print()


    



   







    
    

    

    



