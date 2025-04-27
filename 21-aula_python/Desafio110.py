def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço = 0,moeda = 'R$'):
    return f'{moeda}{preço:>2.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('='*34)
    print('Resumo do valor'.center(30))
    print('='*34)
    print(f'O preço foi analisado:   \t{moeda(preço)}')
    print(f'Preço Dobrado:           \t{dobro(preço, True)}')
    print(f'A metade do preço:       \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento:        \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução:            \t{diminuir(preço, taxar, True)}')
    print('='*34)



    

