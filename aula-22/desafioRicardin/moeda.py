def aumentar(preço=0, taxa=0):
    return preço + (preço * taxa / 100)

def diminuir(preço=0, taxa=0):
    return preço - (preço * taxa / 100)

def dobro(preço=0):
    return preço * 2

def metade(preço=0):
    return preço / 2

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def converter_para_dolar(preço=0, cotacao=5.74):
    return preço / cotacao
