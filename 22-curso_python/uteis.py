def moeda(preco=0, moeda='R$', format = False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def metade(preco=0, format = False):
    r = preco / 2
    return r if format is False else moeda(r)

def dobro(preco=0, format = False):
    r= preco * 2
    return r if format is False else moeda(r)

def maiorPreco(preco=0, taxa=10, format = False):
    r= preco + (preco * taxa / 100)
    return r if format is False else moeda(r)
    
def menorPreco(preco=0, taxa=10, format= False):
    r= preco - (preco * taxa / 100)
    return r if format is False else moeda(r)
