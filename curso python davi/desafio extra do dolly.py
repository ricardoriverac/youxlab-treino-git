nome = str(input('Digite o nome do titular: '))
saldo = float(input('Digite o saldo da conta: '))
maximo = float(input('Qual o valor máximo permitido para saque? '))
print(f'\nOlá {nome}! O saldo de sua conta é R${saldo:.2f}.')
print('=' * 10, 'MENU', '=' * 10)
extrato = []
while True:
    opcao = int(input('''
Escolha uma opção:
    [1] Consultar saldo
    [2] Depositar
    [3] Sacar
    [4] Ver extrato
    [5] Sair
Opção: '''))
    if opcao == 1:
        print(f'Seu saldo atual é R${saldo:.2f}.')
    elif opcao == 2:
        deposito = float(input('Digite o valor do depósito: '))
        if deposito > 0:
            saldo += deposito
            extrato.append(f'Depósito: +R${deposito:.2f}')
            print(f'Depósito de R${deposito:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')
    elif opcao == 3:
        valor_saque = float(input('Digite o valor do saque: '))
        if valor_saque > saldo:
            print('Erro: Saldo insuficiente.')
        elif valor_saque > maximo:
            print(f'Erro: O valor excede o limite de saque permitido (R${maximo:.2f}).')
        elif valor_saque <= 0:
            print('Erro: Valor inválido para saque.')
        else:
            saldo -= valor_saque
            extrato.append(f'Saque: -R${valor_saque:.2f}')
            print(f'Saque de R${valor_saque:.2f} realizado com sucesso.')
    elif opcao == 4:
        print('\n--- EXTRATO ---')
        if not extrato:
            print('Nenhuma movimentação registrada.')
        else:
            for movimento in extrato:
                print(movimento)
        print(f'Saldo atual: R${saldo:.2f}')
        print('----------------')
    elif opcao == 5:
        print('Encerrando o programa... Obrigado por usar nosso sistema!')
        break
    else:
        print('Opção inválida. Tente novamente.')
