import moeda

p = float(input('Digite o preço: R$'))
print(F'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}')
print(F'Reduzindo 13% temos {moeda.diminuir(p, 13, True)}')