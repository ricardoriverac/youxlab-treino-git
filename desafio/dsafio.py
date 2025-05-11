
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

br= []
for i in jogadores:
   if i['nacionalidade'] == 'BR':
        br.append(i["gols"])
soma = 0
for i in br:
    soma+=i

print( f'brasil : {soma/len(br)}')


jp=[]
for i in jogadores:
    if i["nacionalidade"]=='JP':
        jp.append(i["gols"])
somajp=0
for i in jp:
    somajp+=i
print(f'japão : {somajp/len(jp)}')  

argentina= []
for i in jogadores:
    if i['nacionalidade'] == 'AR':
        argentina.append(i["gols"])
somaarg = 0
for i in argentina:
    somaarg+=i
print(f'argentina : {somaarg/len(argentina)}')

usa = []
for i in jogadores:
    if i['nacionalidade'] == 'USA':
        usa.append(i["gols"])
somausa = 0
for i in usa:
    somausa+=i

print(f'usa : {somausa/len(usa)}')


fr= []
for i in jogadores:
    if i['nacionalidade'] == 'FR':
        fr.append(i["gols"])
somafr = 0
for i in fr:
    somafr+=i
print(f'frança : {somafr/len(fr)}')

print('----ranking----')
