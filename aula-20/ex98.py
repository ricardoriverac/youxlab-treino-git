from time import sleep
i = f = p = 0

def contador(inicio,fim,passo, personalizado = ''):
    if personalizado == 'Nn':
        for n in range(inicio,fim,passo):
            print(n,end=' ')
    else:
        print()
        i = int(input('Inicio: '))
        f = int(input('Fim: '))
        p = int(input('Pasoo: '))
        for c in range(i,f,p):
            print(c,end=' ')
            sleep(0.5)
            
print('\nA)')
contador(inicio = 0, fim = 11, passo = 1, personalizado='Nn' )

print()

print('\nB)')
contador(inicio = 10, fim = -2, passo = -2, personalizado='Nn')

print()
print('\nC)')
contador(personalizado = 'Ss', inicio = i , fim = f, passo= p )