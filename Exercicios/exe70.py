#Crie um programa que leia o nome e o preço de varios produtos.
#O programa deverá perguntar se o usuario vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000
#Qual é o nome do produto mais barato.

total = 0
produtoMaisBarato = ""
menorPreco = float("inf")
produtosAcimaDeMil = 0
totalDeItens = 0

while True:
    print("\n-----------------------------------------")
    print("-----------Catalogo de Compra -----------")
    print("-----------------------------------------\n")

    nomeProduto = input("Qual produto você deseja comprar? ")
    precoProduto = float(input("Qual e o preço do produto: "))

    total = total + precoProduto
    totalDeItens += 1

    if precoProduto < menorPreco:
        menorPreco = precoProduto
        produtoMaisBarato = nomeProduto

    if precoProduto > 1000:
        produtosAcimaDeMil += 1

    pergunta = input("Você deseja continuar comprando? [S/N] ").upper()

    if pergunta == "N":
        print("\nVocê finalizou sua compra.")
        print(f"Total: {total}")
        print(f"Total de itens: {totalDeItens}")

        if precoProduto > 1000:
            print(f"Voce teve {produtosAcimaDeMil} produtos acima de R$1.000.")
        
        print(f"Produto mais barato: {produtoMaisBarato}")
        break


