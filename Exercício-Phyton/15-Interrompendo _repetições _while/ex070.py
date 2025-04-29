total_gasto = 0

mais_de_1000 = 0

produto_mais_barato = ''

preco_mais_barato = None

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))

    total_gasto += preco

    if preco > 1000:
        mais_de_1000 += 1

    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Produtos que custam mais de R$1000: {mais_de_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R$ {preco_mais_barato:.2f})")
