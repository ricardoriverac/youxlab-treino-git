def fatorial(num, show):
    f =1
    for c in range(num, 0, +1):
        f *= c
    if show == True:
        for i in range(num, 0, -1):
            print(f'x {i} ', end='')
        return f
    else:
        if show == False:
            print('FIM')
            return f
            


num = int(input('Digite um valor: '))
show = str(input('Quer mostrar o calculo do fatoria? (True ou False)')).upper()
if show == 'T':
    show = bool(True)
else:
    if show == 'N':
        show = bool(False)

print(f'{fatorial(num, show,)}')