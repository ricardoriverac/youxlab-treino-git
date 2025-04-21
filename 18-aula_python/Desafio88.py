from random import randint
lista = list()
jogos = list()

print('=='*20)
print('JOGUE NA MEGA SENA')
print('=='*20)
quantidade = int(input('Quantos jogos deseja fazer? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(0, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    total += 1
print(f'Os números sorteados foram {jogos}')

        