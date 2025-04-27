# PALPITES PARA MEGA SENA
from random import randint
from time import sleep
lista=[]
jogos=[]
quantidade=1
print('VEM JOGAR NA MEGA!')
escolha=int(input('Digite quantos jogos você deseja fazer: '))
while quantidade <=escolha:
    contador=0
    while True:
        numeros=randint(1,60)
        if numeros not in lista:
            lista.append(numeros)
            contador+=1
        if contador>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    quantidade+=1
for indice, l in enumerate(jogos):
    print(f'Jogo {indice+1}: {l}')
    sleep(1)

