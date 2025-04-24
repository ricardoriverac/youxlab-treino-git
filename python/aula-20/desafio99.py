from time import sleep
def maior(*num):
    cont = 0
    mn = 0
    print('='*45)
    print(f'Analizando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
        if c > mn:
            mn = c
        cont += 1
    print(f'/ Foram informados {cont} valores ao todo.')
    print(f'E o maior número listado foi: {mn}')
    sleep(2)
