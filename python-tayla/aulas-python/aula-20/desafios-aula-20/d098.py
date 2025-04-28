from time import sleep

inicio = 0
fim = 0
passo = 0

def linha():
    print('\033[1m-=\033[m' * 20)

def contador(inicio, fim, passo):

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
    for n in range(inicio, fim, passo):
        print(f'{n}', end=' ', flush = True)
        sleep(0.5)
    print('FIM!')
    linha()

contador(1, 10, 1)
contador(10, 0, -2)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)