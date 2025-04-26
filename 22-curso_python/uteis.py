def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def metade(preco=0):
    return preco / 2

def dobro(preco=0):
    return preco * 2

def maiorPreco(preco=0, taxa=10):
    return preco + (preco * taxa / 100)

def menorPreco(preco=0, taxa=10):
    return preco - (preco * taxa / 100)
