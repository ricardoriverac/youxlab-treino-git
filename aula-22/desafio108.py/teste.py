import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 10))}')
