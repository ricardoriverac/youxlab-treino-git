def fatorial(numero,show=False):
    """
    f -- fatorial
    show -- Vai realizar s insd

    """
    f = 1
    for contador in range(numero,0,-1):
        if show:
            print(f'{contador} X ',end =' ')
        if contador == 1:
            print(f' = ', end='')

        f *= contador   
    return f


print(fatorial(5,show = True))    ### Vai fazer isso tudo com o valor entre () "Fatorial(função) + valor"
