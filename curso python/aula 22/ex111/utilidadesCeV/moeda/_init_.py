def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa / 100)
    if formato:
        return moeda(resultado)
    else:
        return resultado

def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa / 100)
    if formato:
        return moeda(resultado)
    else:
        return resultado

def dobro(preco=0, formato=False):
    resultado = preco * 2
    if formato:
        return moeda(resultado)
    else:
        return resultado

def metade(preco=0, formato=False):
    resultado = preco / 2
    if formato:
        return moeda(resultado)
    else:
        return resultado

def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
    print(f'{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, True)}')
    print('-' * 30)
