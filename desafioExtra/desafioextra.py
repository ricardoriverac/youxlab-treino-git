print("=== Banco ===")
nome = input("Digite o nome do titular da conta: ")
saldo = float(input("Digite o saldo inicial da conta: R$ "))
saque_limite = float(input("Digite o limite de saque por operação: R$ "))
extrato = ""
while True:
    print("\n=== Menu ===")
    print("1 - Consultar saldo")
    print("2 - Depositar valor")
    print("3 - Sacar valor")
    print("4 - Ver extrato")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print(f"\nSaldo atual de {nome}: R$ {saldo:.2f}")
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a depositar: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    elif opcao == "3":
        valor_saque = float(input("Digite o valor a sacar: R$ "))
        if valor_saque > saque_limite:
            print(f"Erro: O valor excede o limite de saque por operação (R$ {saque_limite:.2f}).")
        elif valor_saque > saldo:
            print("Erro: Saldo insuficiente para realizar o saque.")
        elif valor_saque <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    elif opcao == "4":
        print("\n=== Extrato da Conta ===")
        if extrato == "":
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato.strip())
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "5":
        print(f"\nObrigado por usar o sistema bancário, {nome}. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção do menu.")