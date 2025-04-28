numeros=[[],[]]
valor = 0

for c in range (1,8):

    valor =int(input('Digite um valor pra entrar em numeros posição 1 ou dois: '))

    if valor %2 == 0:
        numeros[0].append(valor)

    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f'O números pares digitados: {numeros[0]}')
print(f'Os números impares digitados foram: {numeros[1]}')