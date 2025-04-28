menu = 0
maior = 0
menor = 0
n1 = 0
n2 = 0
while not menu == 5:
    n1 = int(input('escolha um número '))
    n2 = int(input('escolha um número '))
    menu = int(input('''
    [1] somar
    [2] multiplicar
    [3] qual deles é maior
    [4] mudar de número
    [5] sair '''))
    if menu == 1:
        soma = n1+n2
        print ('{} + {} = {} '.format(n1, n2, soma))
    if menu == 2:
        multiplicar = n1*n2
        print ('{} x {} = {} '.format(n1, n2, multiplicar))
    if menu == 3:
        if n1 > n2:
            maior = n1
        else:
            if n2 > n1:
                maior = n2
        print ('Entre {} e {} o maior é {}'.format(n1, n2, maior))
print ('você saiu.')