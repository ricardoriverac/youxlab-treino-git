produtos = ("Bolo de cenoura", 5.75, "Bolacha quebra-quebra", 3.00, "Bolo de chocolate", 5.90, "Bolo de aipim", 5.00, "Pudim de leite", 8.00,
            "Bolo de abacaxi", 6.70, "Bolo de brigadeiro", 11.32, "Bolo de morango com cobertura", 8.30, "Bolo de milho", 6.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)