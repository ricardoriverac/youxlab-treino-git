nome= input('Nome do titular da conta: ')
saldo= input('Digite seu saldo inicial: ')
limite= input('Digite seu saque limite: ')
numeros= (1, 4)
menu= (input('====MENU==== \n [1] CONSULTAR SALDO \n [2] DEPOSITAR VALOR \n [3] SACAR VALOR \n [4] SAIR \n'))
if menu == numeros:
    print('Seu saldo atual é: {}'.format(saldo))
    