opçao = 0
saldoinicial = 0
deposito = 0
sacar = 0
deposito1 = list()
sacar = list()
saldoi = list()

print('='*50)
print('                 BANCO X')
print('='*50)
nome = str(input('Digite o nome do Titular: '))
saldoinicial = float(input('Qual o valor da sua conta: '))
saldoi.append(saldoinicial)
limite = float(input('Adicione um limite de saque: '))
print('='*50)

while True:
    print('''Escolha sua opção 
          [ 1 ] Verificar Saldo
          [ 2 ] Deposito
          [ 3 ] Sacar valor
          [ 4 ] Extrato
          [ 5 ] Sair''')
    print('='*50)
    opçao = int(input('Qual sua opção? '))

    if opçao == 1:
        print('='*50)
        print(f'O seu saldo é R${saldoinicial:.2f}')
        print('='*50)

    if opçao == 2:
        deposito = float(input('Quanto quer Depositar? '))
        deposito1.append(deposito)
        print('='*50)
        saldoinicial = saldoinicial + deposito
        print(f'Você depositou R${deposito:.2f}')
        print(f'Você ficou com R${saldoinicial:.2f}')
        print('='*50)

    if opçao == 3:
        sacarm = float(input('Quanto quer sacar? '))
        print('='*50)
        sacar.append(sacarm)

        if sacarm > saldoinicial:
            print('O valor de saque é maior que o seu saldo')
            
        if sacarm > limite:
            print(f'O seu limite é menor que o valor de saque, seu limite é R${limite:.2f}')
            print('='*50)

        else:
            saldoinicial = saldoinicial - sacarm
            print(f'Você sacou R${sacarm:.2f}')
            print(f'Você Ficou com R${saldoinicial:.2f}')
            print('='*50)

    if opçao == 4:
        print('='*50)
        print(f'O seu saldo de início era R${saldoi}')
        print('='*50)
        print(f'Você sacou R${sacar} ')
        print('='*50)
        print(f'Você depositou R${deposito1}')
        print('='*50)
        print(f'Seu saldo é de R${saldoinicial}')
        print('='*50)
        
        

    if opçao == 5:
        break
        
        

  

        
    



