
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
    }
]         
br = []
for i in jogadores:
     if i['nacionalidade'] == 'BR':
         br.append(i['gols'])
soma = 0
for i in br:
    soma += i
media = soma/len(br)
print(f"A media de gols BR é : {media}")

jp = []
for p in jogadores:
    if p ['nacionalidade'] == 'JP':
        jp.append(p['gols'])
    soma = 0 
    for p in jp:
        soma += p
media = soma/len(jp)
print(f"A media de gols JP é : {media}")

usa = []
for u in jogadores:
    if u ['nacionalidade'] == "USA":
        usa.append(u["gols"])
    soma = 0
    for u in usa:
        soma += p 
media = soma/len(usa)
print(f"A media de gols USA é {media}:")

