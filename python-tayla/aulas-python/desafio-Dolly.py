print('\033[1m-=\033[m' * 20)
print('\033[1;33m               BANCO LAB       \033[m')
print('\033[1m-=\033[m' * 20)

extratos = []

nome = input('Digite o nome do titular da conta: ')
saldo = float(input('Qual seu saldo: R$'))
saldoInicial = saldo
limiteSaque = float(input('Qual o limite de saque: R$'))

escolha =  deposito = saque = 0

while True:
    print('')
    print(""" \033[1m-=-=-=-=-= MENU -=-=-=-=-=\033[m
[1] Consultar saldo
[2] Depositar valor
[3] Sacar valor
[4] Extrato
[5] Sair""")
    print('\033[1m-=\033[m' * 13)
    escolha = int(input('Qual é sua escolha? '))
    print('\033[1m-=\033[m' * 13)

    #mostrando saldo
    if escolha == 1:
        print(f'\033[1mSeu saldo é R${saldo:.2f}\033[m')

    #depositando
    if escolha == 2:
        deposito = float(input(f'Qual valor você quer depositar? R$'))
        saldo += deposito
        print('\033[1;32mDeposito feito com sucesso!\033[m')
        extratos.append(f'Deposito: {deposito}')

    #sacando
    if escolha == 3:
        saque = float(input('Qual valor você quer sacar? R$'))

        if saque > limiteSaque:
            print('\033[1;31mValor de saque indisponível\033[m')
            saldo = saldo
        elif saque > saldo:
            print('\033[1;31mValor de saque indisponível\033[m')
            saldo = saldo
        else:
            print('\033[1;32mSaque feito com sucesso\033[m')
            saldo -= saque
            extratos.append(f'Saque: {saque}')

    #extrato
    if escolha == 4:
        print(f'\033[1mSaldo inicial: {saldoInicial}')

        for extrato in extratos:
            print(extrato)

        print(f'Saldo atualizado: R${saldo}\033[m')

    if escolha == 5:
        print('\033[1;36mVolte sempre ao BANCO LAB!\033[m')
        break