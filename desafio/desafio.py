print ("<<<<<<<<<<<<<<< CONTA BANCÁRIA >>>>>>>>>>>>>>>")
soma = 0
nome = str (input("Qual o nome do titular da conta ? "))
saldo = float (input ("Saldo inicial da conta ? "))
limite = float (input("Qual o limite de saque permitido por operação: "))
valorDepositado = 0
valorsaque = 0
saldoatualizado = 0
list = [ ]
list.append(f" Nome: {nome}")
list.append(f" saldo: {saldo}")
print ("\t-----" * 4)
while True:
 
    print ("\t-----" * 4)
    print ("<<<<<<<<<< MENU >>>>>>>>>>")
    print("""
    [1] Consultar saldo; 
    [2] Depositar valor;
    [3] Sacar valor;
    [4] Sair do programa.
    [5] Extrato
        """)
    print ("\t-----" * 4)
    opcao = int (input("Qual a opção desejada ? "))
    if opcao == 1:
        print (f"R$ \033[36m{saldo:.2f}\033[m ")
        
    elif opcao == 2:
        valorDepositado = float (input("Qual valor vai ser depositado ? "))
        soma = saldo + valorDepositado
        saldo = soma
        list.append(f' Deposito: {valorDepositado}')
        print (f"Seu saldo agora é de:  \033[36m{soma}\033[m ")
    elif opcao == 3:
        valorsaque = float (input ("Qual valor você deseja sacar ? "))
        if valorsaque > limite:
            print (f"Você não pode sacar essa quantia, precisar ser menor que  \033[36m{limite}\033[m  ")
        if valorsaque > saldo:
            print ("Saldo insuficiente, tente uma quantia menor.")
        elif valorsaque <= limite:
            saldoatualizado = saldo - valorsaque
            saldo = saldoatualizado
            list.append(f" Saque: {valorsaque}")
            list.append(f" Saldo Atualizado: {saldoatualizado}")
            print (f"você sacou  \033[36m{valorsaque}\033[m , seu saldo agora é de \033[36m{saldoatualizado}\033[m")
    elif opcao == 4:
        print ("\033[32mTchauu, volte sempre!!!\033[m")
        break
    elif opcao == 5:

        print ("<<<<<<< EXTRATO >>>>>>>")
        for l in list:
            print(l)
    else:
        print ("\033[34mOpção inválida, digite novamente!\033[m")
