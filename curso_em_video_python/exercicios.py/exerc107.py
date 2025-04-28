import uteis

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {uteis.metade(preco)}')
print(f'O dobro de {preco} é {uteis.dobro(preco)}')
print(f'Com 10% de juros é R${uteis.maiorPreco(preco):.2f}')
print(f'Com 10% de desconto é R${uteis.menorPreco(preco)}')