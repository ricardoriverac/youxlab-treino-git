import moeda

p = float(input('Digite o preço: R$'))
print(F'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10)}')
print(F'Reduzindo 13% temos {moeda.diminuir(p, 13)}')