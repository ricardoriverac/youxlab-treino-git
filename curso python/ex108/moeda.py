def aumentar(preco=0, porcentagem=0):
    return preco + (preco * porcentagem / 100)

def diminuir(preco=0, porcentagem=0):
    return preco - (preco * porcentagem / 100)

def dobro(preco=0):
    return preco * 2

def metade(preco=0):
    return preco / 2

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
