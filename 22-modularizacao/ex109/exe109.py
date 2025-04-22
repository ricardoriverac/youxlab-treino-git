import moeda

p = float(input('Digite um vaalor: '))
print(f'A metade de {moeda.formatar(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.dobro(p,False)}')
print(f'O valor aumentado deu {moeda.aumentar(p,10,False)}')
print(f'O valor dimunuido deu {moeda.diminuir(p,13,True)}')