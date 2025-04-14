def contador(inicio , fim , passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    print(f'-='*20)
    if inicio < fim:
        for c in range(inicio , fim+1 , passo):
            print(f'{c}',end=' ')
        print()
    if inicio > fim :
            for c in range(inicio , fim-1 , -passo):
                print(f'{c}',end=' ')
            print()
        

#programa principal
print('-='*30)
print('Contagem de 1 até 10 de 1 em 1')
print('-='*30)
for c in range(1, 11):
    print(f'{c}',end=' ')
print('FIM!')
print('-='*20)
print('Contagem de 10 até 0 de 2 em 2')
print('-='*20)
for cont in range(10,-1,-2):
    print(f'{cont}',end=' ')
print('FIM!')
print('-='*20)
print('Agora e a sua vez de personalizar...')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
contador(inicio , fim , passo)