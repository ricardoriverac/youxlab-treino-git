import moeda
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco, 13, True)}')
