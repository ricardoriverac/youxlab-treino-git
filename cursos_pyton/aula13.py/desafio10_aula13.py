maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'qual peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {} kg e o menor peso {} kg'.format(maior, menor))