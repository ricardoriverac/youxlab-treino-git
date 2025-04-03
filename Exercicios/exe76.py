#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia
#No final, mostre uma listagem de preços, organizando os dados em forma tabular

tabelaDeProdutos = ("Arroz", 25.50, "Feijão", 9.25, "Macarrão", 5.70)

print("-" * 40)
print("------=-=-= Lista de produtos =-=-=-----")
print("-" * 40)

for pos in range(0, len(tabelaDeProdutos)):
    if pos % 2 == 0:
        print(f"{tabelaDeProdutos[pos]:.<30}", end="")
    else:
        print(f"R${tabelaDeProdutos[pos]:>7.2f}")
print("-" * 40)

# for p in range(5):
#     nomeProduto = input("Digite o nome de um produto: ")

#     tabelaDeProdutos = tabelaDeProdutos + (nomeProduto,)

# print(f"\nLista de produtos: {tabelaDeProdutos}")

