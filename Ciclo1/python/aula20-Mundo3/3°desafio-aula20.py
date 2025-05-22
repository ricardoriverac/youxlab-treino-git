#FUNÇÃO DE CONTADOR
from time import sleep
def contador(inicio, fim ,passo):
    if passo<0:
        passo*=-1
    if passo==0:
        passo=1
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')
    count=inicio
    if inicio<fim:
        while count<=fim:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count+=passo
        print('Fim!')
    else:
        while count>=fim:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count-=passo
        print('Fim!')    
contador(1,10,1)
contador(10,0,2)
print('Sua vez!')
inicio=int(input('Início: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
contador(inicio,fim,passo)