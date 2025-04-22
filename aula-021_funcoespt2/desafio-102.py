def fatorial(num, show=0):
    f =1
    for c in range(num, 0, +1):
        f *= c
    if show == True:
        for i in range(num, 0, -1):
            print(f'x {i} ', end='')
    else:
        if show == False:
            print('FIM')

    return f
            


num = int(input('Digite um valor: '))
show = bool(input('Quer mostrar o calculo do fatoria? (True ou False)'))
print(f'{fatorial(num, show,),}')