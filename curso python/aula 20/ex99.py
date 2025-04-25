def maior(*numeros):
    print('Analisando os valores...')
    if len(numeros) == 0:
        print('Nenhum valor foi informado.')
    else:
        maiorValor = numeros[0]
        for numero in numeros:
            if numero > maiorValor:
                maiorValor = numero
        print(f'Foram informados \033[34m{len(numeros)}\033[m valores: \033[33m{numeros}\033[m')
        print(f'O maior valor é \033[35m{maiorValor}\033[m')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()