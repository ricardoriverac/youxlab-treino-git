def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa / 100)
    return moeda(res) if format else res


def diminuir(preco=0, taxa=0, formatar=False):
    res = preco - (preco * taxa / 100)
    return moeda(res) if format else res


def dobro(preco=0, formatar=False):
    res = preco * 2
    return moeda(res) if format else res


def metade(preco=0, formatar=False):
    res = preco / 2
    return moeda(res) if format else res


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo} {preco:,.2f}'.replace('.', ',').replace(',', 'v', 1).replace(',', '.').replace('v', ',')


def resumo(preco=0, taxa_aum=10, taxa_red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço:  \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aum}% de aumento:\t{aumentar(preco, taxa_aum, True)}')
    print(f'{taxa_red}% de redução:\t{diminuir(preco, taxa_red, True)}')
    print('-' * 30)