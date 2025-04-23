listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,

            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,

            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)



print('-'*34)

print('{:^34}'.format('LISTAGEM DE PREÇÕS'))

print('-'*34)

for contador1 in range(0, len(listagem), 2):

    print(f'{listagem[contador1]:.<24} R$ {listagem[contador1+1]}')