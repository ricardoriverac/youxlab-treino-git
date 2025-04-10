lista = []
cont9 = 0
contPar = 0
numPares = []
for i in range(4):
    numero = int(input('Digite um número: '))
    lista.append(numero)
    par = numero % 2
    if par == 0:
        numPares.append(numero)
    if 9 in lista:
        cont9 += 1
if 3 in lista:
    tres = lista.index(3)
    print(f"o número 3 apareceu pela primeira vez na posição {tres}")
else:
    print('O número 3 não esta nessa lista!')
print (lista)
print(f'O número 9 apareceu {cont9} vezes.')
# print(f'O número 3 apareceu pela primeira vez na posição {tres}')
print(f'Os números pares são: {numPares}')
