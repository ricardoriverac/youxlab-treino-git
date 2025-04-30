menor = 0
maior = 0
for pessoas in range(1, 6):
    pesos = float(input(f'Digite o peso da {pessoas}ª: '))
    if pessoas == 1:
        menor = pesos
        maior = pesos
    else:
        if pesos < menor:
            menor = pesos
        if pesos > maior:
            maior = pesos
print (f'O maior peso é de {maior:.1f}kg e o menor peso é de {menor:.1f}kg. ')