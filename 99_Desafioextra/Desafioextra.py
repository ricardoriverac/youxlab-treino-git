nome = str(input("Qual do titular da conta?: "))
saldo = float(input("Qual seu saldo atual?: "))
saque = float(input("Qual limite de saque?: "))
opçoes = 0
valor = 0
saques2 = 0
while opçoes != 4:
    print("[===]" *9)
    print('''[1]Consultar saldo
[2]Depositar valor
[3]Sacar valor
[4]Sair''')
    opçoes = int(input("Qual sua escolha: "))
    if opçoes != 1 and opçoes != 2 and opçoes != 3 and opçoes != 4:
        print("Dados invalidos, tente novamente")
    elif opçoes == 1:
        print(f"O seu saldo atual e {saldo}")
    elif opçoes == 2:
        valor = float(input("Qual valor voce deseja depositar: "))
        valoratual= saldo + valor
        saldo = valoratual 
        print("===" *9)
        print("Saldo atualizado com sucesso")
        print("===" *9)
    elif opçoes == 3:
        saque2= float(input("Digite o valor do saque: "))
        saldoatual = saldo - saque2
        saldo = saldoatual
        if saque2 >= saque:
            print("===" *9)
            print("Erro chegou ao limite de saque")
            print("===" *9)
        elif saque2 >= saldo:
            print("Erro saque e maior que a quantidade de valor na conta")
            print("===" *9)
        else:
         print("===" *9)
         print("Saque feito com sucesso")
         print("===" *9)
         saque2 - saldo  
