maior=0
menor=0
for c in range(1,6):
    peso=float(input('O peso da primeira pessoa: '))
    if maior == 0 or peso > maior:
        maior = peso 
    if menor ==0 or peso < menor:
        menor = peso
print('O maior peso e {} '.format(maior))
print('O menor peso e {} '.format(menor))
