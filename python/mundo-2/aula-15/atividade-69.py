def cadastro_pessoas():
    mais_de_18 = 0
    homens = 0
    mulheres_menos_20 = 0

    while True:
        print("\n--- Cadastro de Pessoa ---")
        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Digite uma idade válida!")
            continue

        sexo = ""
        while sexo not in ['M', 'F']:
            sexo = input("Sexo [M/F]: ").strip().upper()

        if idade > 18:
            mais_de_18 += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres_menos_20 += 1

        continuar = ""
        while continuar not in ['S', 'N']:
            continuar = input("Deseja cadastrar outra pessoa? [S/N]: ").strip().upper()

        if continuar == 'N':
            break


    print("\n=== RESULTADO FINAL ===")
    print(f"A) Total de pessoas com mais de 18 anos: {mais_de_18}")
    print(f"B) Total de homens cadastrados: {homens}")
    print(f"C) Total de mulheres com menos de 20 anos: {mulheres_menos_20}")

cadastro_pessoas()
