numero = int(input('Quantos termos você quer mostrar?: '))

n = 0
n2 = 1

print(f'{n} -> {n2} ', end= '' )

cont = 3

while cont <= numero:
    t3 = n + n2

    print(f'-> {t3}', end= '')
    n = n2 
    n2 = t3
    cont += 1
