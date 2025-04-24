maior = 0
menor = float('inf')
for i in range(5):
    p = float(input('Digite o kg:'))
    if p>maior:
        maior = p
    if p<menor:
        menor = p
print(f'Dentre esses, o maior peso foi {maior}kg e o menor foi {menor}kg ')
