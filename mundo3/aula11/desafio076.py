produtos = (
    'Pão', 1.50,
    'Leite', 4.20,
    'Café', 9.99,
    'Arroz', 19.90,
    'Feijão', 7.80,
    'Óleo', 6.75,
    'Macarrão', 3.50,
    'Açúcar', 2.89,
    'Sal', 1.10,
    'Farinha', 4.50
)
print('-' * 40)
print(f'{"LISTA DE PREÇOS :D":^40}')
print('-' * 40)

for listinha in range(0, len(produtos), 2):
    nome = produtos[listinha]
    preco = produtos[listinha + 1]
    print(f'{nome:.<30} R$ {preco:>7.2f}')

print('-' * 40)