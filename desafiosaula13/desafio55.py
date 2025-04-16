maior = 0
menor = 0
lista = [ ]
for c in range(0,5):
    peso = float(input('Qual seu peso?: '))
    lista.append(peso)
    if peso<menor or c==0:
        menor=peso
    if peso>maior:
        maior=peso
print('O maior peso é {} e o menor peso é {} '.format(maior, menor))
