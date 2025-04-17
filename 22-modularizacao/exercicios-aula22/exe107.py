from utilizaveis import moeda
p = float(input('Digite o valor: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'O valor aumentado deu {moeda.aumentar(p,10)}')
print(f'O valor dimunuido deu {moeda.diminuir(p,13)}')

