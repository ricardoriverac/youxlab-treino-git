import moeda

preco = float(input('Digite o preço: R$'))
print(f'Aumentando 10% de {moeda.format(preco)} temos {moeda.format(moeda.aumentar(preco))}')
print(f'Diminuindo 15% de {moeda.format(preco)} temos {moeda.format(moeda.diminuir(preco))}')
print(f'O dobro de {moeda.format(preco)} é {moeda.format(moeda.dobro(preco))}')
print(f'A metade de {moeda.format(preco)} é {moeda.format(moeda.metade(preco))}')