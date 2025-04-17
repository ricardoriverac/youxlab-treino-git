produtos = (("Arroz", 10.00), ("Feijão", 7.50),("Miojo", 3.0), ("Chocolate", 8.56), ("Carne", 30.00), ("Batata", 17.50))
print("-" * 30)
print ("\033[32m\tLISTAGEM PRODUTOS\033[m")
print("-" * 30)
print("\033[34mPRODUTOS\033[m   |  \033[34mPREÇOS\033[m")
print("-" * 30)
for produto, preco in produtos:
    print(f"{produto:<10} | R$ {preco:>5.2f}")
