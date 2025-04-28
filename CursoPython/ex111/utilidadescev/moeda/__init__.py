def aumentar(preco=0, taxa=0):
    return preco + (preco * taxa / 100)

def diminuir(preco=0, taxa=0):
    return preco - (preco * taxa / 100)

def dobro(preco=0):
    return preco * 2

def metade(preco=0):
    return preco / 2

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \tR${preco:.2f}')
    print(f'Dobro do preço: \tR${dobro(preco):.2f}')
    print(f'Metade do preço: \tR${metade(preco):.2f}')
    print(f'{taxa_aumento}% de aumento: \tR${aumentar(preco, taxa_aumento):.2f}')
    print(f'{taxa_reducao}% de redução: \tR${diminuir(preco, taxa_reducao):.2f}')
    print('-' * 30)
