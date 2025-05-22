from time import sleep

def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    
    if passo == 0:
        passo = 1 
    
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont += abs(passo)
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont -= abs(passo)
    print('FIM!')
    print('-' * 30)

contador(1, 100, 1)

contador(100, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
