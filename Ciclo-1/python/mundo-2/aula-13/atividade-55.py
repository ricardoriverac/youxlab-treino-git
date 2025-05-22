maior = 0
menor = float('inf')
for i in range(5):
    peso = float(input('Peso: '))
    if peso>maior:
        maior = peso
    if peso<menor:
        menor = peso
print(f'Dentre esses, o maior peso foi {maior}kg e o menor foi {menor}kg ')