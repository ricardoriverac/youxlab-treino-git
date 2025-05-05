from time import sleep
r = 0 
nome = str(input('Digite o seu nome: '))
saldo_inicial = float(input('Digite seu saldo inicial, {}: '.format(nome)))
limite = float (input('Qual seu limite de saque? '))
while r != 4:
    r = int(input('''
Qual operação você deseja realizar ?
    [1] Consultar saldo:
    [2] Depositar valor:
    [3] Sacar valor:
    [4] Sair:
     '''))
    if r ==1:
        saldo_inicial
        print(f'Seu saldo é {saldo_inicial}')

    elif r == 2:
        depositar = float(input("Quantos reais você gostaria de depositar? "))
        saldo_inicial += depositar
        saldo_inicial=saldo_inicial+depositar

    elif r ==3:
        sacar = float(input('Quantos reais você gostaria de sacar? '))
        if sacar > limite:
            print('O valor excede o limite do saque  ')
        elif sacar > saldo_inicial:
            print('ERRO, saldo insuficiente. ')
        else:
            saldo_inicial-= sacar
            print('saque realizado sucesso')

    elif r == 4:
        print("obrigada por usar o sistema, volte sempre! ♡ ")