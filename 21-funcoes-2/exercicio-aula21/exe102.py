def fatorial(n,show):
    """
    param n: O numero do fatorial
    param show: e um valor (opcional)
    param return: retorna o valor do fatorial 
    """
    print('-='*30)
    fac = 1
    if show == True:
        for c in range(n,0,-1):
            print(f'{c}x',end=' ')
    for c in range(n,0,-1):
        fac *= c
    return fac


#programa principal

print(fatorial(5 , True))
