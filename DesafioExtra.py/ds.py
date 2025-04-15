nomeT = 0
SaldoI = 0
Limit =0
op=0
Dep=list()
Ret=list()


print('>>>>>>>Bem-Vindo ao seu Banco Digital<<<<<<<')
print('~' * 45)
nomeT=str(input('Nome do Titular Da conta: '))
Limit=float(input('Limite De saque:  '))
SaldoI=float(input('Qual o seu Saldo Inicial: '))
print('~' * 45)
while True:
    print(''' Quais dessas opções:
      [ 1 ]-Consultar Saldo
      [ 2 ]-Depositar Saldo
      [ 3 ]-Sacar Valor
      [ 4 ]-Sair
      [ 5 ]- Extrato
       ''')
    op=int(input('Qual das opções você deseja? '))
    if op == 4:
            break
    if op == 1:
            print('==' * 20)
            print(f'Seu saldo é: {SaldoI} ')
            print('==' * 20)
    if op == 2:
            print('==' * 20)
            Adicionar=float(input('Quanto que você quer depositar? '))
            Dep.append(Adicionar)
            print('==' * 20)
            SaldoI= Adicionar+ SaldoI
    if op == 3:
            print('==' * 20)
            Sacar=float(input('Qual o valor que deseja sacar?  '))
            Ret.append(Sacar)
            print('==' * 20)
            SaldoI= SaldoI - Sacar
            if Sacar > SaldoI:
                   print('Pobre')
            if Sacar > Limit:
                print('Seu limit e menor que o saque')
                SaldoI= SaldoI - Sacar
            
    if op == 5:
           print('==' * 20)
           print(f'O valor depositado foi {Dep}')
           print('==' * 20)
           print(f'Seu valor retirado foi {Ret}')
           print('==' * 20)
        
