lista = ('suco natural', 1.75,
'chá', 3.00,
'cacau 90%', 60.00,
'morango', 17.90,
'batata', 4.20,
'manteiga', 29.99,
'ceral', 320,
'miojo', 9.90,
'bolo', 99.90)
print('\033[35mLISTAGEM DE PREÇO')
for c in range(0, len(lista), 2):
    print(f'{lista[c].title():40}R${lista[c+1]:8.2f}')