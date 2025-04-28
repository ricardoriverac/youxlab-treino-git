def aumentar(preco,taxa):
    reais = preco + (preco * taxa/100)
    return reais
    

def diminuir(preco,taxa):
    reais = preco - (preco * taxa/100)
    return reais


def dobro(preco):
    reais = preco * 2
    return reais


def metade(preco):
    reais = preco/2
    return reais

