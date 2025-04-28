from time import sleep

def contador(inicio, fim, passo):

    print('=' * 45)

    print(f'A contagem de {inicio} até {fim} de {passo} em {passo}: ')

    sleep(1)

    if inicio < fim:

        for i in range(inicio,fim+1,passo):

            print(f'{i}.. ', end='')

            sleep(0.3)

        print('FIM!')

    elif inicio > fim:

        for i in range(inicio,fim-1,-passo):

            print(f'{i}.. ', end='')

            sleep(0.3)

        print('FIM!')



contador(1,10,1)

contador(10,0,2)




print('=' * 45)

print('Agora é sua vez de personalizar a contagem!')

i = int(input('Qual é o valor inicial? '))

f = int(input('Qual é o valor final? '))

pas = int(input('Qual o valor do passo? '))

contador(i,f,pas)

print('=' * 45)