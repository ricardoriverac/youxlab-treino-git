extrato = []
depositou = []
sacou = []

print('--'*35)
print('CAIXA LAB'.center(70))
print('--'*35)

nome = str(input('Nome do titular da conta: '))
saldo = float(input('Saldo inicial da conta: R$'))
limiteDeSaque = float(input('Qual será o limite de saque por operação? R$'))
extrato.append([f'Saldo inicial: {saldo:.2f}'])

while True:
    print('--'*35)
    opcao = int(input('''
[ 1 ] CONSULTAR SALDO
[ 2 ] DEPOSITAR VALOR
[ 3 ] SACAR VALOR
[ 4 ] SAIR
[ 5 ] EXTRATO
                      
OPÇÃO: '''))
    
    if opcao == 1:
        print('--'*35)
        print(f'Seu saldo atual é de R${saldo:.2f}')
    elif opcao == 2:
        deposito = float(input('Quanto você deseja depositar? R$'))
        saldo += deposito
        extrato.append([f'Depositou: {deposito}'])

    elif opcao == 3:
        saque = float(input('Qual valor você deseja sacar? R$'))

        if saque > limiteDeSaque:
            print('Valor maior que o limite de saque. Tente novamente.')

        elif saque > saldo:
            print('Saldo indisponível para saque. Tente novamente.')

        else:
            saldo -= saque
            extrato.append([f'Sacou: {saque}'])

    elif opcao == 4:
        print('FINALIZANDO O SISTEMA, ATÉ MAIS! ...')
        break
    elif opcao == 5:
        print('--'*35)
        print('EXTRATO'.center(70))
        print('--'*35)
        for i in extrato:
            print(i)
        print(f'Saldo atual: R${saldo:.2f}')
           
    else:
        print('Opção indisponível, tente novamente.')