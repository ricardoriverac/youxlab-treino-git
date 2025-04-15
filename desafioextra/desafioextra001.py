import time

def interface():
    cadastro = []
    transacoes = []

    info = dict()
    info['nome'] = input('Nome do titular: ').title().strip()
    info['saldo'] = float(input('Insira seu saldo inicial: '))
    info['limite_saque'] = float(input('Insira seu limite de saque: '))
    cadastro.append(info)

    print('-' * 30)
    print(f'Olá, {info["nome"]}')
    print('-' * 30)

    while True:
        try:
            resp = int(input('''Escolha como prosseguir: 
[1] Consultar Saldo
[2] Depositar valor
[3] Sacar valor
[4] Extrato
[5] Sair
Escolha: '''))
            print('-' * 30)

            if resp == 1:
                print(f'Seu saldo atual é: R$ {info["saldo"]:.2f}')
            elif resp == 2:
                valor = float(input('Digite o valor a depositar: R$ '))
                info['saldo'] += valor
                transacoes.append(f'Depósito: R$ {valor:.2f}')
                time.sleep(1)
                print(f'Depósito realizado. Novo saldo: R$ {info["saldo"]:.2f}')
            elif resp == 3:
                valor = float(input('Digite o valor a sacar: R$ '))
                if valor <= info['saldo'] and valor <= info['limite_saque']:
                    info['saldo'] -= valor
                    transacoes.append(f'Saque: R$ {valor:.2f}')
                    time.sleep(1)
                    print(f'Saque realizado. Novo saldo: R$ {info["saldo"]:.2f}')
                else:
                    print('Saque não permitido. Verifique o saldo e o limite de saque.')
            elif resp == 4:
                print('EXTRATO DE TRANSAÇÕES'.center(40, '='))
                if transacoes:
                    for i, t in enumerate(transacoes, 1):
                        print(f'{i}. {t}')
                else:
                    print('Nenhuma transação realizada ainda.')
                print('=' * 40)
            elif resp == 5:
                print('Saindo da conta...')
                time.sleep(1)
                print(10 * '=', 'VOLTE SEMPRE', 10 * '=')
                break
            else:
                print('Opção inválida. Tente novamente.')
            print('-' * 30)
        except ValueError:
            print("Por favor, insira um número válido.")

interface()