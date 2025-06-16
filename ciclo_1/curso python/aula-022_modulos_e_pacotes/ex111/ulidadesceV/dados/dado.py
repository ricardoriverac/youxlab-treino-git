def resumo(num, porcent1, porcent2):
    dobro = num * 2
    metade = num / 2
    taxa = (porcent1/100) + 1
    aumento = num * taxa
    dimi = 1 - (porcent2/100)
    diminui = num * dimi
    print('-=' *30)
    print('        RESUMO DO VALOR          ')
    print('-=' *30)
    print(f'A metade de {num} é {metade}')
    print(f'O dobro de {num} é {dobro}')
    print(f'O aumento em {porcent1} de {num} é {aumento}')
    print(f'O valor reduzido em {porcent2} de num é {diminui}')
    print('-=' *30)



def leia_dinheiro(num):
    num