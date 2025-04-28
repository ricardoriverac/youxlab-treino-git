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
    return f'{simbolo}{preco:.2f} '.replace('.',',')

def resumo(preco = 0,taxaAumento = 0,taxaReducao = 0):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)

    print(f'Dados do valor {moeda(preco)}')
    print('-'*30)

    print(f'0 dobro é:\t\t{dobro(preco,True)}')
    print(f'A metade é:\t\t{metade(preco,True)}')
    print(f'Aumentado pela taxa:\t{aumentar(preco,taxaAumento,True)}')
    print(f'Diminuido pela taxa:\t{diminuir(preco,taxaReducao,True)}')
