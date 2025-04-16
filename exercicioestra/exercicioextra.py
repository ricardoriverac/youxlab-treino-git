print('-='*20)
print('\033[1;36mCONSULTE SUA CONTA BANCÁRIA\033[m')
print('-='*20)
saldoAtualizado = 0
saldoComSaque = 0
saldoInicial = 0
nome = input('Qual o \033[35mNOME TITULAR\033[m da conta?: ')
saldo = float(input('Qual seu \033[35mSALDO INICIAL\033[m?: '))
limite = float(input('Qual o \033[35mLIMITE DE SAQUE\033[m permitido por operação?: '))
saldoInicial = saldo
lista = []
while True:
    print('''ESCOLHA UMA DAS OPÇÕES: 
          \033[36m[1]Consultar saldo; 
          \033[35m[2]Depositar valor;
          \033[34m[3]Sacar valor;
          \033[33m[4]Sair;\033[m
          \033[32m[5]Ver extrato;\033[m''')
    opcao = int(input('Qual opção você escolhe?: '))
    
    if opcao==4:
        print(f'\033[31mPROGRAMA ENCERRADO!\033[m Volte sempre {nome}')
        break
    
    elif opcao==1:
        print(f'''NOME:{nome}
              SALDO ATUAL:R${saldo:.2f}''')
        
    elif opcao==2:
        valorDepositado = float(input('Qual valor você deseja \033[35mDEPOSITAR?\033[m: '))
        saldoAtualizado=saldo+valorDepositado
        print(f'Seu saldo atual é de {saldoAtualizado}')
        saldo=saldoAtualizado
        lista.append(f'Deposito: R${valorDepositado}')
        
    elif opcao==3:
        valorSacado = float(input('Qual valor você deseja \033[35mSACAR?\033[m: '))
        saldoAtualizado = saldo-valorSacado
        print(f'Seu saldo atual é de R${saldoAtualizado}')
        saldo=saldoAtualizado
        lista.append(f'Sacado: R${valorSacado}')
        if valorSacado>limite:
            print('Esse valor \033[31mNÃO pode ser sacado\033[m! Tente novamente')
            
    elif opcao==5:
        print('-='*20)
        print('\033[1;35mSEU EXTRATO:\033[m')
        print(f'Saldo inicial: R${saldoInicial}')
        for mov in lista:
            print(mov)
        print(f'Saldo atualizado: R${saldoAtualizado}')
        print('-='*20)