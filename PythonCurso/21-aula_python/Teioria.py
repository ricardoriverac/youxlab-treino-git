def contador(i, f, p):
    """
    faz uma contagem e mostra na teal
    i: inicio da contagem
    f: final da contagem
    p: passo da conatgem
    
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print(' FIMM !!!!!!!!!!')

contador(0, 100, 10)


def contador2(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é igual a {s}')



contador2(2, 1)
