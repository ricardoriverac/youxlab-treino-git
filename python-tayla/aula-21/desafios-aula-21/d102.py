def fatorial(numero, show = False):
    numeroFatorial = 1

    for c in range(numero, 0, -1):
        numeroFatorial *= c
        if show == True:
            print(f'{c} x', end=' ')
            if c == 1:
                print('=', end=' ')
    return numeroFatorial

print('-=' * 20)
print(fatorial(5, show = True))