import ds107

preco = float(input('Digite o preço: R$ ' ))
print(f'A metade de {preco} é {ds107.metade(preco)}')

print(f'O dobro de {preco} é {ds107.dobro(preco)}')

print(f'Com o aumento de 10% fica {ds107.aumentar(preco,10)}')

print(f'')