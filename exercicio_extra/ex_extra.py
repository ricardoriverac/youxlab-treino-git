deposito= 0
saque= 0
nome= input('Nome do titular da conta: ')
saldo= int(input('Digite seu saldo inicial: '))
limite= int(input('Digite seu saque limite: '))
for a in range(1, 3):
    menu= int(input('===MENU===\n [1] CONSULTAR SALDO \n [2] DEPOSITAR VALOR \n [3] SACAR VALOR \n [4] SAIR \n SELECIONE UMA OPÇÃO: '))
    if menu == 1:
      print('SEU SALDO É {}'.format(saldo))
    elif menu == 2:    
       deposito= int(input('DEPOSITE UM VALOR: '))
    calculo1= saldo + deposito 
if menu == 3 and limite > saque:
  saque= int(input('VALOR DO SAQUE: '))
  print('ERRO!! VALOR SUPERIOR AO SAQUE LIMITE!')