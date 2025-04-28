extrato=[]
saldoNovo=0
saldoPermitido=0
deposito=0
sacando=0

nome=str(input('Digite seu nome: '))
saldo = float(input('Digite seu saldo atual R$: '))
extrato.append(f'O saldo inicial foi: {saldo}')
saldoPermitido=float(input('Digite seu limite para sacar R$: '))
#dep=[]
#sac=[]

while True:

    print( )

    escolha=input('''Escolha uma das opções: 
            [1] Consulte seu saldo
            [2] Depositar Valor)
            [3] Sacar Valor
            [4] Sair
            [5] Consultar Extrato
            Escolha sua opção: ''')

    if escolha == '1':
        
        print('<>'*20)

        print(f' {saldo} ')

    if escolha == '2':
        deposito= int(input('Digite o valor a ser adicionado: '))

        saldoNovo=saldo + deposito
        saldo=saldoNovo

        extrato.append(f'depósito: {deposito} ')

    if escolha == '3':
         sacando=int(input('Digite o valor a ser sacado: '))
         
         if sacando > saldoPermitido:
            print('Erro') 

         else: 
            saldoMenor = saldo - sacando
            saldo = saldoMenor

            extrato.append(f'saque: {sacando} ')
    

    if escolha == '4':
        print('Transações terminadas. Tenha um Bom Dia! ')
        break

    if escolha == '5':

        print('------EXTRATO------')

        for registro in extrato:
            print(registro)

        print('<>'*20)

 






