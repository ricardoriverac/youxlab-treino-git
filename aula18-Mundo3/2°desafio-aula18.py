#NÚMEROS ÍMPARES E PARES
numeros=[[],[]]
valor=0
for contador in range(1,8):
    valor=int(input(f'Digite o {contador}° valor: '))
    if valor%2==0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
print(f'Pares: {numeros[0]}')
numeros[1].sort()
print(f'Ímpares: {numeros[1]}')
