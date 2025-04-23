from random import randint
lista = list()
jogos = list()
print ('-=' * 17)
print ('      \033[35mMEGA SENA\033[m     ')
print ('-=' * 17)
quantidade = int (input('\033[34mQuantos jogos você quer que eu sorteei ?\033[m '))
total = 1
while total<= quantidade:
    contador = 0
    while True:
        numero = randint (1,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print ('-=' * 4, f'sorteando {quantidade} jogos','-=' * 4 )
print (' \033[34mOs números sorteados foram\033[m')
print ('-=' * 17)
for indice , lista in enumerate(jogos):
    print (f'Jogo {indice+1}: {lista}')
print ('-=' * 17)


