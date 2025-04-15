def cadastro_produtos():
    total_gasto = 0
    produtos_mais_1000 = 0
    produto_mais_barato = ''
    menor_preco = None

    while True:
        print("\n--- Cadastro de Produto ---")
        nome = input("Nome do produto: ").strip()

        try:
            preco = float(input("Preço: R$"))
        except ValueError:
            print("Digite um valor válido para o preço.")
            continue

        total_gasto += preco

        if preco > 1000:
            produtos_mais_1000 += 1

        if menor_preco is None or preco < menor_preco:
            menor_preco = preco
            produto_mais_barato = nome

        continuar = ""
        while continuar not in ['S', 'N']:
            continuar = input("Deseja cadastrar outro produto? [S/N]: ").strip().upper()

        if continuar == 'N':
            break

    print("\n=== RESUMO DA COMPRA ===")
    print(f"A) Total gasto na compra: R${total_gasto:.2f}")
    print(f"B) Número de produtos que custam mais de R$1000: {produtos_mais_1000}")
    print(f"C) Produto mais barato: {produto_mais_barato} (R${menor_preco:.2f})")


cadastro_produtos()