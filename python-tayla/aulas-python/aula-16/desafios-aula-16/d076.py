listagem = ('Arroz', 26.90, 'Feijão', 7.99, 'Batata', 4.99, 'Alface', 3.70, 'Tomate', 6.00, 
            'Ovo', 17.00, 'Chocolate', 8.00, 'Sorvete', 25.00, 'Doce de leite', 9.0)

print('\033[1m-\033[m' * 40)
print('\033[1;33m            LISTA DE PREÇOS          \033[m')
print('\033[1m-\033[m' * 40)

cont = len(listagem)
produto = 0
preco = 1

while True:
    if cont == 0:
        break

    print(f'{listagem[produto]:.<30} R${listagem[preco]:>7.2f}')

    cont -= 2
    produto += 2
    preco += 2

print('\033[1m-\033[m' * 40)