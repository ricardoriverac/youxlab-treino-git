# Faça um programa que tenha uma função chamada 'contador()', que receba três parâmetros: inicio, fim e passo e realize a contagem. seu programa tem que realizar três contagens através
# da função criada:
# a) de 1 até 10, pulando de 1 em 1
# b) de 10 até 0, pulando de 2 em 2
# c)uma contagem personalizada 
# faça isso pensando em python porem não mostre o código mas me ajuda a pensar em um solução para esse problema
# from time import sleep
# def contador(inicio, fim, passo):
#     cont = inicio
#     for c in range(inicio, fim + 1, passo):
#         cont += 1
#         print(cont)
#         sleep(0.5)
#     print('FIM')
from time import sleep

def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')

    if passo == 0:
        passo = 1
    if inicio < fim:
        # Contagem crescente
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += abs(passo)
    else:
        # Contagem decrescente
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= abs(passo)
    print('FIM!')
    print('-=' * 20)


# a) De 1 até 10, de 1 em 1
contador(1, 10, 1)

# b) De 10 até 0, de 2 em 2
contador(10, 0, -2)

# c) Contagem personalizada
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)




# cont = 0
# for c in range(0, 10):
#     cont += 2
#     print(cont)
#     if cont == 10:
#         break
# contador(inicio = 1, fim = 10, passo = 1)
# contador(inicio = 10, fim = 0,passo = 2)