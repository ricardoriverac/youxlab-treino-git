primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    soma = primeiroNumero + segundoNumero
    multiplicacao = primeiroNumero * segundoNumero
    print ("""
        O que você deseja fazer?
        [ 1 ] - Somar os números
        [ 2 ] - Multiplicar os números
        [ 3 ] - Descobrir qual é o maior número
        [ 4 ] - Entrar com novos números
        [ 5 ] - Sair do programa""")
    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        print (f'A soma de {primeiroNumero} + {segundoNumero} é igual a {soma}')
    elif opcao == 2:
        print (f'A multiplicação de {primeiroNumero} e {segundoNumero} é de {multiplicacao} ')
    elif opcao == 3:
        if primeiroNumero > segundoNumero:
            print (f'O maior número é o {primeiroNumero} ')
        elif segundoNumero > primeiroNumero:
            print (f'O maior número é o {segundoNumero} ')
        else:
            print ('Ambos os números são iguais. ')
    elif opcao == 4:
        primeiroNumero = int(input('Digite o primeiro número: '))
        segundoNumero = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print ('Tudo bem, até mais! ')