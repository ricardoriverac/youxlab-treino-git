from ex112.utilidadesCeV.dados import dado, moedas


try:
    num = dado.leia_dinheiro()
    porcent1 = int(input('Por quanto você quer aumentar o valor? '))
    porcent2 = int(input('Por quanto você quer diminuir o valor? '))
    moedas.resumo(num, porcent1, porcent2)

except ValueError as erro:
    print(f'Erro {erro}')

