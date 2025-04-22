from time import sleep 
lista = dict()
goool = []
lista['nome'] = str(input('Nome do jogador: '))
cartaoAmarelo = 0
cartaoVermelho = 0
cartoesTotal = 0
expulso = False
jogosExpulsos = 0
partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))

sleep(0.3)
print('-' *40)
sleep(0.3)

for jogos in range(1, partidas+1):
    if expulso:
       print('\033[1;31mVOCÊ TÁ EXPULSO MUHAHAHAHA\033[m')
       jogosExpulsos +=1
       expulso = False
    else:
        gol = int(input(f'Quantos gols {lista["nome"]} fez na {jogos}° partida? '))
        goool.append(gol)
        lista['cartao'] = str(input('Recebeu cartão amarelo? [S/N] ')).upper()
        if lista['cartao'] in 'S':
            cartoes = int(input('Quantos? '))
            cartoesTotal += cartoes
            if cartoes >=2:
                print('\033[1;31mVOCÊ FOI EXPULSOOOO KKKKKKK\033[m')
                jogos+=2
                cartoesTotal = 0
                expulso= True
                
            if cartoes == 1:
                cartaoAmarelo += cartoes
        
                if cartaoAmarelo >=3:
                    print('\033[1;31mVOCÊ FOI EXPULSOOOO KKKKKKK\033[m')
                    jogos+=2
                    cartaoAmarelo = 0
                    expulso = True

            
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
print(f'\033[1;31mFoi expulso {jogosExpulsos} vezes.')
