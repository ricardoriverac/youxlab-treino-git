print('\033[1;34m-=-=-=-=-= Bem vindo(a) ao nosso banco!  =-=-=-=-=-\033[m')

nome = str(input('Olá, qual o seu nome? : '))
saldo = float(input('Qual seu saldo inicial? : '))
limite = int(input('Qual será o limite de saque da sua operação? : '))
valorD = []
valorS = []

while True:
    print('Opções abaixo ⬇⬇⬇\n[1] Consultar saldo\n[2] Depositar valor\n[3] Sacar valor\n[4] Ver extrato\n[5] Sair')
    escolha = str(input('Qual opção deseja? : '))
    if escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4' and escolha != '5':
        while escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4' and escolha != '5':
            escolha = int(input(f'\nErro, digite novamente! : '))
        
    if escolha == '1':    
        print(f'Seu saldo é R${saldo}')
        
    if escolha == '2':
        deposito = int(input('Valor do deposito: R$'))
        saldo = deposito + saldo
        valorD.append(deposito)
        
    if escolha == '3':
        saque = float(input('Valor do saque: R$'))
        valorS.append(saque)
        if saque > saldo:
            saque = float(input('Você não tem tanto dinheiro assim..\nDigite novamente: R$'))
            valorS.append(saque)
        
        if saque > limite:
            print(f'Seu limite de saque é: R${limite}')
            saque = float(input('Valor do saque: R$'))
            saldo = saldo - saque
            valorS.append(saque)
   
    if escolha == '4':
        print(F'----------------------------------\nVocê depositou esses valores: {valorD}')
        print(F'Você sacou esses valores: {valorS}')
        print(F'Seu saldo é R${saldo}\n----------------------------------')
    
    if escolha == '5':
        print('\033[1;34m-=-=-=-=-= Programa encerrado, até mais!! =-=-=-=-=-\033[m')
        break
    