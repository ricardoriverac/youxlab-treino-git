def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco, taxa_aumento=10, taxa_reducao=10):
    print('~' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('~' * 40)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_reducao}% de desconto: \t{menorPreco(preco, taxa_reducao, True)}')
    print(f'{taxa_aumento}% de aumento: \t{maiorPreco(preco, taxa_aumento, True)}')
    print('~' * 40)

def metade(preco=0, format=False):
    r = preco / 2
    return r if not format else moeda(r)

def dobro(preco=0, format=False):
    r = preco * 2
    return r if not format else moeda(r)

def maiorPreco(preco=0, taxa=10, format=False):
    r = preco + (preco * taxa / 100)
    return r if not format else moeda(r)

def menorPreco(preco=0, taxa=10, format=False):
    r = preco - (preco * taxa / 100)
    return r if not format else moeda(r)
