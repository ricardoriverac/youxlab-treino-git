from time import sleep
r = 0
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o Segundo número: '))
while r != 5:
    r = int(input('''
    Escolha qual operação você vai fazer
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
'''))
    if r == 1:
        soma = numero1 + numero2
        print('A soma de {} + {} = {}.'.format(numero1, numero2, soma))
    elif r == 2:
        multiplicação = numero1 * numero2
        print('A multiplicação entre {} e {} é {}.'.format(numero1, numero2, multiplicação))
    elif r == 3:
        if numero1 > numero2:
            print('O numero 1 = {} é maior que o numero 2 = {}.'.format(numero1, numero2))
        else:
            print('O numero 2  = {} é maior que o numero 1 = {}.'.format(numero2, numero1))
    elif r == 4:
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o Segundo número: '))
    elif r == 5:
        sleep(1)
    else:
        print('erro')
