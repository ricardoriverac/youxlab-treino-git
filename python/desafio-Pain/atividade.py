cadastro = {}
banco = ''
extrato = []
cadastro['nome'] = input('Digite seu nome: ')
cadastro['saldo'] = float(input('Digite seu saldo inicial: '))
cadastro['limite'] = float(input('Digite o limite de saque: '))
while True:
    print('-' * 30)
    banco = input('''
1 - Consultar saldo
2 - Depositar valor
3 - Sacar valor
4 - Extrato
5 - Sair
Escolha uma opção: ''')

    if banco == '1':
        print(f"Saldo atual: R$ {cadastro['saldo']:.2f}")
    elif banco == '2':
        deposito = float(input('Digite o valor a depositar: '))
        cadastro['saldo'] += deposito
        extrato.append(f"Depósito: +R$ {deposito:.2f}")
        print(f"Depósito realizado. Novo saldo: R$ {cadastro['saldo']:.2f}")
    elif banco == '3':
        saque = float(input('Digite o valor a sacar: '))
        if saque <= cadastro['limite'] and saque <= cadastro['saldo']:
            cadastro['saldo'] -= saque
            extrato.append(f"Saque: -R$ {saque:.2f}")
            print(f"Saque realizado. Novo saldo: R$ {cadastro['saldo']:.2f}")
        else:
            print('Saque negado. Verifique o saldo ou o limite.')
    elif banco == '4':
        print(f"Saldo atual: R$ {cadastro['saldo']:.2f}")
        print('Extrato de transações:')
        if not extrato:
            print('Nenhuma transação realizada.')
        else:
            for item in extrato:
                print(item)
        print(f"Saldo atual: R$ {cadastro['saldo']:.2f}")
    elif banco == '5':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    print('-' * 30)