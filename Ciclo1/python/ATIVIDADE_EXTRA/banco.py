nome=str(input('Nome do titular da conta:')).strip()
saldo=float(input('Seu saldo atual:'))
valor=0
limite=float(input('Limite de saque permitido:'))
while True:
    print('MENU\n'
    '1- Consultar saldo \n'
    '2- Depositar valor\n'
    '3- sacar valor\n'
    '4- sair')
    escolha=int(input('Escolha:'))
    if escolha==1:
        print('Seu saldo é de:{:.2f}'.format(saldo))
    if escolha==2:
        valor=float(input('Valor que deseja depositar: '))
        saldo+=valor
    if escolha==3:
        valor=float(input('Valor que deseja sacar: '))
        if valor>limite:
            print(f'ERRO\n O valor desejado ultrapassa o limite de saque que é de {limite}')
            saldo=saldo
        else:
            saldo-=valor
    if escolha==4:
        break
