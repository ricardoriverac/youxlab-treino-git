soma = 0
quantidade = 0

for c in range(1, 5):
    numero = int(input(f'Digite o {c}º número: '))
    soma += numero
    quantidade += 1

media = soma / quantidade
print(f'A média é {media:.2f}')
