cheaper_name = ""
somador = higher = cheaper = 0

while True:
    name = str(input("Nome do produto: \n"))
    price = float(input("Preço: \n"))
    
    somador += price

    if price > 1000:
        higher += 1
    
    if cheaper == 0:
        cheaper = price
        cheaper_name = name
    elif price < cheaper:
        cheaper = price
        cheaper_name = name

    choice = str(input("Inserir mais produtos? [S / N] \n")).strip().upper()
    
    if choice == "N":
        print(f"Total gasto: R${somador:.2f}")
        print(f"Produtos que custam mais do que R$1.000: {higher}")
        print(f"O produto mais barato é {cheaper_name}, que custa R${cheaper:.2f}")
        break