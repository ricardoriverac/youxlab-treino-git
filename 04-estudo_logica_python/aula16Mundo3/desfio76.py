lista = ('agua',3.80,
         'suco', 2.99,
         'banana', 15.90,
         'miojo', 5.25,
         'arroz', 35.00)
print('\033[35m---------LISTAGEM DE PREÇO--------')
for t in range(0, len(lista),2):
    print(f'{lista[t].title():40}R${lista[t+1]}')

