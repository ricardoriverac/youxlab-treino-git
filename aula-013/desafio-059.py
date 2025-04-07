while True:
    soma = 0
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite outro número"))

    soma = n1 + n2
    m = n1 * n2




    print('Menu:')
    menu = int(input('[1] somar \n [2] Multiplicar \n [3] Maior /n [4] Novos numero \n [5] Sair do programa'))
    while menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        print('Não exite essa opção')
        menu = int(input('          [1] somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n [5] Sair do programa'))

    else:
        if menu == 1:
            print(f'Você escolheu somar')
            print(f'A soma desses números é {soma}')
        elif menu == 2:
            print('Você escolheu multiplicar!')
            print(f'A Multiplicação desses números é: {m} ')
        elif menu == 3:
            print("Você escolheu mostrar o maior!")
            if n1 > n2:
                print(f'O maior número é o {n1}')
            else:
                print(f'o maior número é o {n2}') 
        elif menu == 4:
            continue
        elif menu == 5:
            break
