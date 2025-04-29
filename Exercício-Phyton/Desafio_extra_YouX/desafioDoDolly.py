Saldo = 0

sair = 'S'

DadosN = str(input('Nome do Titular da conta: '))

DadosG = float(input('Qual o saldo da conta?: '))

DadosL = float(input('Qual o limite de saque?: '))

while Saldo != 4: 

    print (' ')
    
    Saldo = int(input('''O que deseja conferir?:
                      
        [ 1 ]  Consultar Saldo           
        [ 2 ]  Depositar Valor
        [ 3 ]  Sacar valor              
        [ 4 ]  Sair                         
        : '''))
    
    print('<=>'*20)

    if  Saldo == 1:
        print(f'Seu saldo é R${DadosG}')

    elif Saldo == 2:
        valor = int(input('Qual valor quer depositar?: '))
        saldo = DadosG + valor 
        print (f'Seu Saldo é R${saldo}')
        DadosG = saldo 

    elif Saldo == 3:
        saque = int(input('Qual valor do saque?: '))
        if saque > DadosL:
            print('erro de limite.')
        else: 
            saldo = DadosG - saque
            print(f'Voce tem R${saldo} de saldo.')
            DadosG = saldo 

print('VOLTE SEMPRE.')
        