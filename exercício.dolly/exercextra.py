from time import sleep 
print ('-' * 40)
nomeBanco = ('\033[1;35mBANCO DA ANA\033[m' )
print (f'{nomeBanco:^50}')
print('-' *40)

nome = str(input('\033[1mDigite o nome do titular da conta:\033[m '))
saldo = float(input('\033[1mDigite o seu saldo atual:\033[m '))
limite = float(input('\033[1mQual o limite de saque permitido por operação?\033[m '))
opcao = 0
print ('-' *40)

while opcao!=4:
        print('\033[1mVeja as seguintes opçoẽs:\033[m')
        print('\033[1;35m[1]\033[m Consultar saldo. ')
        print('\033[1;35m[2]\033[m Depositar valor. ')
        print('\033[1;35m[3]\033[m Sacar valor. ')
        print('\033[1;35m[4]\033[m Sair. ')
        print ('-' * 40)
        opcao = int(input('Digite o número que corresponde a sua escolha: '))
        if opcao ==2:
            deposito= float(input('Digite o valor que deseja depositar: '))
            sleep(1)
            saldo = saldo + deposito
            print('\033[1;45mDEPOSITADO.\033[m')
            sleep(0.5)
            print('-' * 40)
        if opcao ==3:
         sacado = float(input('Digite o valor que deseja sacar: '))
         print('\033[1;35mSACANDO...\033[m')
         if sacado > limite:
            print('\033[1;31mPassou do limite.\033[m')
            sleep(1)
         else:
            saldo = saldo - sacado
         
        if opcao ==1:
            sleep(2)
            print(f'\033[1mSeu saldo é de R${saldo}\033[m ')
            sleep(2)
            print('-' * 40)
        if opcao ==4:
            print('\033[1;31mSAINDO...')
            sleep (2)
print ('-' * 40)
print('\033[1;45mCarregando...\033[m ')
sleep (2)
print ('-' * 40)
