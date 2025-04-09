primeiroNumero = int(input('Digite um valor: '))
segundoNumero = int(input('Digite outro valor: '))
opcao = 0
maiorNumero = 0
while opcao != 5:
    print('ESCOLHA UMA OPÇÃO: ')
    print('[1]SOMAR')
    print('[2]MULTIPLICAR')
    print('[3]MAIOR')
    print('[4]NOVOS NÚMEROS')
    print('[5]SAIR DO PROGRAMA')
    opcao = int(input('Escolha uma das opções: '))
    if opcao==1:
        soma = primeiroNumero+segundoNumero
        print('A {}SOMA{} desses números é {}'.format('\033[35m', '\033[m',soma))
    elif opcao==2:
        multiplicacao = primeiroNumero*segundoNumero
        print('A {}MULTIPLICAÇÃO{} desses dois números é {} '.format('\033[35m', '\033[m',multiplicacao))
    elif opcao==3:
        if primeiroNumero>segundoNumero:
            print('O {}MAIOR{} número é {} '.format('\033[35m', '\033[m', primeiroNumero))
        else:
            print('O {}MAIOR{} número é {} '.format('\033[35m', '\033[m', segundoNumero))
    elif opcao==4:
        print('Informe os números novamente: ')
        primeiroNumero = int(input('Digite um valor: '))
        segundoNumero = int(input('Digite outro valor: '))
    elif opcao==5:
        print('{}Finalizando...{}'.format('\033[33m', '\033[m'))
    else:
        print('Opção ínvalida, tente novamente')
print('Fim do programa! Volte sempre! ')




