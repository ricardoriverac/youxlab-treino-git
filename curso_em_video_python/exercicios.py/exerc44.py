from time import sleep
print('Você comprou um produto!')
preco = float(input('Qual é o preço do produto? R$'))
print('AGUARDE...')
sleep(2)
print('Qual vai ser sua forma de pagamento? ')
opcao1 = print('[1]Á vista/cheque: 10% de desconto')
opcao2 = print('[2]Á vista no cartão: 5% de desconto')
opcao3 = print('[3]Em até 2x no cartão: sem desconto')
opcao4 = print('[4]3x ou mais no cartão: 20% de juros')
escolhido = int(input('Escolha: '))
print('CALCULANDO...')
sleep(2)
if escolhido ==1 :
    print('No total, você vai pagar R${:.2f}'.format(preco * (90/100)))
elif escolhido ==2 :
    print('No total você irá pagar R${:.2f}'.format(preco * (95/100)))
elif escolhido ==3 :
    print('Você irá pagar R${:.2f} por mês.'.format(preco / 2))
elif escolhido ==4 :
    print ('Você irá pagar R${:.2f} no total.'.format(preco*(120/100)))
print('\033[4;33mOBRIGADA PELA COMPRA!')