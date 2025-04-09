nome = str(input('Bem vindo a loja, qual o seu nome? '))
produtos = []
produtos1000 = 0
menorProduto = ''
menor = 9999999
while True:
    nomeProduto = str(input("Digite o nome do seu produto: "))
    preco = float(input(f"Digite o valor de {nomeProduto}: "))
    continuar = str(input(f"Você quer continuar? {nome} S/N")).upper()
    produtos.append(preco)
    if preco > 1000:
        produtos1000 += 1
    
    if preco <= menor:
        menor = preco
        menorProduto = nomeProduto



    if continuar != 'S':
        break
# print(f'\n Lista de produtos:')
# for product in produtos:
#     print(f"{product['nomeProdutos']} - {product['preco']} preco")
somaProdutos = sum(produtos)
print(f"O valor gasto na sua compra foi de R${somaProdutos}")
print(f'Há {produtos1000} produtos que custam mais de R$1000,00')
print(f'O produto mais barato é o {menorProduto} custando R${menor}:')


