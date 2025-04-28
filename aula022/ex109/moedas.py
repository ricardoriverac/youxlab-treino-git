def aumentar(preco,taxa,formato):

    reais = preco + (preco * taxa/100)
    return reais if formato is False else moeda(reais)


def diminuir(preco,taxa,formato = True):

    reais = preco - (preco * taxa/100)
    return reais if formato is False else moeda(reais)


def dobro(preco,formato = True):

    reais = preco * 2
    return reais if formato is False else moeda(reais)


def metade(preco,formato = True):

    reais = preco/2
    return reais if formato is False else moeda(reais)


def moeda(preco = 0,simbolo ='R$' ):
    return f'{simbolo}{preco:.2f} '.replace('.',',')    ##Duvida
