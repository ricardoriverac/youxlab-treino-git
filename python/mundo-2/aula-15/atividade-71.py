def caixa_eletronico():
    print("="*30)
    print("{:^30}".format("CAIXA ELETRÔNICO"))
    print("="*30)

    try:
        valor = int(input("Qual valor você deseja sacar? R$"))
    except ValueError:
        print("Por favor, digite um valor inteiro válido.")
        return

    cedulas = [50, 20, 10, 1]
    print("\nCédulas entregues:")

    for cedula in cedulas:
        quantidade = valor // cedula
        valor %= cedula
        if quantidade > 0:
            print(f"{quantidade} cédula(s) de R${cedula}")

    print("="*30)
    print("Volte sempre!")

caixa_eletronico()
