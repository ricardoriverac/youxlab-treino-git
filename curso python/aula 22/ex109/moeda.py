def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res

def dobro(preco=0, formato=False):
    res = preco * 2
    if formato:
        return moeda(res)
    else:
        return res

def metade(preco=0, formato=False):
    res = preco / 2
    if formato:
        return moeda(res)
    else:
        return res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
