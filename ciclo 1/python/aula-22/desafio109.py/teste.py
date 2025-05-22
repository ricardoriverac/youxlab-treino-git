import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p,True)}')
print(f'Aumentando 10% de {p} é {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 10% de {p} é {moeda.diminuir(p, 10, True)}')
