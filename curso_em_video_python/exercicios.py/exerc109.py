from uteis import moeda, metade, dobro, maiorPreco, menorPreco

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preco)} é {metade(preco, True)}')
print(f'O dobro de {moeda(preco)} é {dobro(preco, True)}')
print(f'Com 10% de juros é {maiorPreco(preco, 10, True)}')
print(f'Com 10% de desconto é {menorPreco(preco, 10, True)}')
