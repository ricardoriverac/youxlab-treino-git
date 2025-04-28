from time import sleep
def maior(*num):
    cont = maior = 0
    print('='*60)
    print('Processando')
    for valor in num:
        print(f'{valor}', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f' - Foram colocados {cont} valores ao todo!! ', end='')
    print(f' - o maior valor foi {maior}')




maior(2, 7, 8, 20)
maior(1, 3, 5)
maior(3, 5, 7)

