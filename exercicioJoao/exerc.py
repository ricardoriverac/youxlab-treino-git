from time import sleep
def enfeite():
    texto = ('\033[1;34mMÉDIA DE GOLS POR NACIONALIDADE\033[m')
    print('~' * len(texto))
    print(texto)
    print('~' * len(texto))

enfeite()
br = []
jp = []
usa = []
fr = []
ar = []

jogadores = [
    {"nome": "Ricardo", "gols": 5, "nacionalidade": "BR"},#ok
    {"nome": "Walter", "gols": 7, "nacionalidade": "BR"}, #ok
    {"nome": "Japa", "gols": 12, "nacionalidade": "JP"}, #ok
    {"nome": "Joao", "gols": 9, "nacionalidade": "JP"}, #ok
    {"nome": "Augusto", "gols": 2, "nacionalidade": "USA"}, #ok
    {"nome": "Cesar", "gols": 5, "nacionalidade": "USA"}, #ok
    {"nome": "Kaio", "gols": 2, "nacionalidade": "JP"},#ok
    {"nome": "Lucas", "gols": 4, "nacionalidade": "BR"},#ok
    {"nome": "Felipe", "gols": 8, "nacionalidade": "BR"},#ok
    {"nome": "Takeshi", "gols": 6, "nacionalidade": "JP"},#ok
    {"nome": "Yuki", "gols": 10, "nacionalidade": "JP"},#ok
    {"nome": "Max", "gols": 3, "nacionalidade": "USA"}, #ok
    {"nome": "Julien", "gols": 7, "nacionalidade": "FR"},
    {"nome": "Pierre", "gols": 5, "nacionalidade": "FR"},
    {"nome": "Emiliano", "gols": 2, "nacionalidade": "AR"},#ok
    {"nome": "Ricardo Jr.", "gols": 9, "nacionalidade": "BR"}, #ok
    {"nome": "Santos", "gols": 1, "nacionalidade": "BR"}, #ok
    {"nome": "Gabriel", "gols": 3, "nacionalidade": "USA"}, #ok
    {"nome": "Mauricio", "gols": 6, "nacionalidade": "AR"}#ok
]

for jogador in jogadores:
    nacionalidades = (jogador['nacionalidade'])
    if nacionalidades in 'BR':
        br.append(jogador['gols'])
    elif nacionalidades in 'JP':
        jp.append(jogador["gols"])
    elif nacionalidades in 'USA':
        usa.append(jogador["gols"])
    elif nacionalidades in 'FR':
        fr.append(jogador["gols"])
    elif nacionalidades in 'AR':
        ar.append(jogador["gols"])

    

mediaBR = sum(br)/len(br)
mediaJP = sum(jp)/len(jp)
mediaUSA = sum(usa)/len(usa)
mediaFR = sum(fr)/len(fr)
mediaAR = sum(ar)/len(ar)

total = {"Brasil": mediaBR, "Japão": mediaJP, "Estados Unidos": mediaUSA, "França": mediaFR, "Argentina": mediaAR}
for k,v in total.items():
    print(f'\033[1;34m{k}\033[m: \033[1mMédia\033[m= {v:.1f}')


    