def contador(i , f, p):
    """
    :i=Inicio
    :f=Fim da contagem
    :p=Passo
    
    
    """
    c = i
    while  c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')
help(contador)