import uteis
from time import sleep

logs = []

login = "João"
senhaBase = "joao1010#br"

uteis.linha()
uteis.cabecalho1("BANCO X")
uteis.linha()
acesso = input("Digite o seu login de acesso: ")
senha = input("Digite a sua senha de acesso: ")

if acesso != login or senha != senhaBase:
    print("\nAcesso negado.")
else:
    print("\nAcesso liberado.")

    uteis.linha()
    test = uteis.cabecalho1(f"Bem - vindo {login}")
    uteis.linha()
    cadSaldo = int(input("Digite o seu saldo bancario: "))
    cadLimite = float(input("Digite o seu limite bancario "))

    while True:
        sleep(0.5)
        uteis.cabecalho2("Menu", "1 - Ver saldo", "2 - Ver limite", "3 - Depositar", "4 - Sacar", "5 - Retirar Extrato", "6 - Sair")
        uteis.linha()
        
        pergunta = int(input("Digite a opção desejada: [1 / 2 / 3 / 4 / 5 / 6] "))

        if pergunta == 1:
            print(f"Saldo: {cadSaldo}")

        elif pergunta == 2:
            print(f"Limite: {cadLimite}")

        elif pergunta == 3:
            addSaldo = float(input("Digite a quantidade do deposito: "))
            calDeposito = cadSaldo + addSaldo
            cadSaldo = calDeposito
            print("Deposito concluido.")
            logs.append(f"Deposito: {addSaldo}")

        elif pergunta == 4:
            efeSaque = float(input("Digite a quantidade de saque: "))

            if efeSaque > cadLimite:
                print("ERRO! Quantia acima do limite.")
            else:
                print("Saque efetuado.")
                saldoAtual = cadSaldo - efeSaque
                cadSaldo = saldoAtual
                print(f"Seu saldo restante: {cadSaldo}")
                logs.append(f"Saque: {efeSaque}")

        if pergunta == 5:
            uteis.linha()
            uteis.cabecalho1("Extrato X")
            for e in logs:
                print(e)
            uteis.linha()
            uteis.cabecalho1("Finalizando o extrato")
            uteis.linha()
            sleep(0.5)

        if pergunta == 6:
            uteis.linha()
            uteis.cabecalho1("Obrigado pela preferencia, volte sempre.")
            uteis.linha()
            break

        

