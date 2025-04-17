from time import sleep
from random import randint
lista = list()
jogos = list()
print('==' * 20)
print('       Mega Cena        ')
print('==' * 20)
quant=int(input('Quantos jogos vocẽ quer fazer?  '))
tot = 1
while tot  <= quant:
    cont=0
    while True:
        num= randint(1 , 60)
        if not num  in lista:
            lista.append(num)
            cont+= 1
        if cont >=6 :
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=  1
print('=' * 3 , f' SORTEANDO  {quant} JOGOS ' , '=' * 3)
for i ,  l in  enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=' * 5 , '< BOA SORTE >' , '=' * 5)