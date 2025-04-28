from time import sleep
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
op= 0
while op != 5:
    print('-=-'*20)
    print('''Quais das opções:
          [ 1 ]- SOMAR
          [ 2 ]- MULTIPLICAR
          [ 3 ]- MAIOR
          [ 4 ]- NOVOS NUMEROS
          [ 5 ]- SAIR DO PROGRAMA''')
    print('-=-'*20)
    op =int(input('Qual sua escolha? '))
    if op == 1:
        soma=n1 + n2
        print('A soma foi {}, os numeros que você escolheu foi {}, {}'.format(soma , n1 , n2))
    if op == 2:
        multi= n1 * n2
        print('A multiplicação foi {}, os numeros que você escolheu foi {}, {}'.format(multi , n1 , n2))
    if op == 3:
        if n1 > n2:
            maior= n1
        elif n1<n2:
            maior=n2
        print('Entre {} é {} , o maior foi {}'.format(n1 , n2 , maior))       
    if op == 4:
        print('Informe os numeros de novo:')
        n1=int(input('Digite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: '))
    elif op == 5:
        print('-=-' *20)
        print('Fim Do Programa')
    else:

        print('Numero invalido')
sleep(2)
print('Obrigado por testar!!!')