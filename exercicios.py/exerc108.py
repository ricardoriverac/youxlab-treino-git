from uteis import moeda, metade, dobro, maiorPreco, menorPreco

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Com 10% de juros é {moeda(maiorPreco(preco))}')
print(f'Com 10% de desconto é {moeda(menorPreco(preco))}')
