#LISTAS DE PREÇOS EM TUPLAS
print('NOTA DE COMPRA')
larguraTot=60
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for i in range (0, len(listagem), 2):
    produtos = listagem[i]
    preco=listagem[i+1]
    pontos='.'*(larguraTot-len(produtos)-len(f'{preco:.2f}'))
    print(f'{produtos}{pontos} R${preco:.2f}')



