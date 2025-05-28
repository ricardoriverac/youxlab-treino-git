import moeda2
p = ''
print('-=-'*15)
p = float(input(f'Digite o preço - {moeda2.moeda(p)}'))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}.')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.dobro(p))}.')
print(f'Aumentando 10%, temos {moeda2.moeda(moeda2.aumentar(p, 10))}.')
print(f'Diminuindo 10%, temos {moeda2.moeda(moeda2.diminuir(p, 10))}.')
print('-=-'*15)