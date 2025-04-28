from time import sleep
def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} a {f} de {p} em {p} ')
    sleep(3)
    
    if p < 0:
        p *= -1
        
    if p == 0:
        p = 1
        
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont+=p
        print('FIM!')
        print()
    else: 
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont-=p
        print('FIM!')
    
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de \033[36mpersonalizar a contagem!\033[m ')    
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))  
contador(inicio, fim, passo)
print('-='*20)
