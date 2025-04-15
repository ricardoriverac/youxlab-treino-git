dic = dict()
gols = []
totalG = 0

nome = str(input('Nome do jogador: '))
dic["nome"] = nome

partidas = int(input(f'Total de partidas de {nome}: '))
dic["partidas"] = partidas

for c in range (partidas):
    g = int(input(f'Quantos gols {dic["nome"]} fez na partida {c+1}? '))
    gols.append(g)
    
    totalG += g
    dic["totalG"] = totalG 

print('--'*35)
print(f''' Nome é {dic["nome"]}
Gols foram {gols}
Teve um total de {dic["totalG"]} gols''')
print('-='*35)
print(f'O jogador {dic["nome"]} jogou {dic["partidas"]} partidas.')
for p in range (partidas):
    print(f'-> Na partida {p+1}, fez um total de {gols[p]} gols')
