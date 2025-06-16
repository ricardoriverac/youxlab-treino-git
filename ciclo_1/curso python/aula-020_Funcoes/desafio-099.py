def maior(*valores):
    maiorValor = 0
    for valor in valores:
        if valor > maiorValor:
            maiorValor = valor
    print(f'O maior valor de {valores} é {maiorValor}')


maior(1, 3, 5, 6, 7, 8,)
maior(4, 5, 4, 3, 4, )
