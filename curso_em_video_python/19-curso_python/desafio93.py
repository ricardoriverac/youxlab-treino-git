from time import sleep 
lista = dict()
goool = []
lista['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))

sleep(0.3)
print('-' *40)
sleep(0.3)

for jogos in range(1, partidas+1):
    gol = int(input(f'Quantos gols {lista["nome"]} fez na {jogos}° partida? '))
    goool.append(gol)
lista['gols'] = goool
lista['total'] = sum(goool)

print('-' *40)

print (lista)
sleep(1)
for k, v in lista.items():
    print(f'O campo {k} tem {v}')
    sleep(1)

print('-' *40)

print(f'O jogador {lista["nome"]} jogou {partidas} jogos. ')

for q, v in enumerate(lista['gols']):
    print(f'Na {q+1}° partida {lista["nome"]} fez {v} gols')
    sleep(0.5)
print(f'Foi um total de {lista["total"]} gols. ')
