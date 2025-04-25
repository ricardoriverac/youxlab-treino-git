def banco():
    print('-=' *30)
    nome = str(input('Nome do titular: '))
    saldo = float(input('Saldo inicial da conta?'))
    limite = float(input('Limite de saque: '))
    carteira = []
    menu = 0
    deposito = 0
    extrato = []
    vezesSaque = 0
    vezesDeposito = 0
    saldoSaque = []
    saldoDeposito = []
    valorDeposito = []
    valorSaque = []
    while True:
        menu = int(input('1 Consultar saldo; \n 2 Depositar valor; \n 3 Sacar valor; \n 4 Sair \n 5 Extrato '))
        if menu == 1:
            print(f'Seu saldo é de {saldo}')
        elif menu == 2:
            depositar = float(input('Quanto você quer depositar? '))
            deposito = saldo + depositar
            saldo = deposito
            vezesDeposito += 1
            extrato.append(f'Depósito: +R${depositar:.2f}')
            saldoDeposito.append(saldo)
            valorDeposito.append(depositar)
            print (f'Você depositou {depositar} e o sldo total ficou em {saldo}')
            extrato.append(f'O saldo atual é de {saldo:.2f} ')
        elif menu == 3:
            sacar = float(input('Quanto você quer sacar? '))
            if sacar > limite:
                print(f'Seu limite é de {limite} não será possivel realizar a operação')
            elif sacar <= limite:
                saque = saldo - sacar
                saldo = saque
                vezesSaque += 1
                extrato.append(f'Saque: -R${sacar:.2f}')
                extrato.append(f'O saldo atual é de {saldo:.2f} ')
                saldoSaque.append(saldo)
                valorSaque.append(sacar)
                print(f'você sacou {sacar} e seu saldo total foi para {saque}')
        elif menu == 5:
            print('EXTRATO')
            saldo -= saque
            for c in extrato:
                 print(c)
            # print(f'Saldo atual: R${saldo :.2f}')
            # print('----------------')
        elif menu == 4:
            break
banco()
    
    
    #    print('Dentro dessa operação você:')
    #    print(f'sacou {vezesSaque} vezes {saldoSaque}')
    #    print(f'Depositou {vezesDeposito} vezes {saldoDeposito}')


