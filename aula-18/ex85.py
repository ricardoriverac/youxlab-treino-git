par = []
impar = []
for n in range(0,7):
    valor = int(input(f'Digite o {n+1}º valor '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
print('=-'*20)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')