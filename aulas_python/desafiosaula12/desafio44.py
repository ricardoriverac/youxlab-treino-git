preco = float(input('Qual o valor do produto?: '))
comDesconto = (preco * (90/100))
comDisconto5 = (preco * (95/100))
comJuros = preco * (120/100)
print('[1] A vista/ dinheiro ou cheque ')
print('[2] A vista no cartão ')
print('[3] Em até 2 vezes no cartão ')
print('[4] 3x ou mais no cartão ')
escolha = int(input('Escolhe uma das opções acima como forma de pagamento: '))
if escolha == 1:
    print('Você tem 10% de desconto! Com esse disconto você paga {} '.format(comDesconto))
elif escolha == 2:
    print ('Você tem 5% de desconto! Com esse desconto você paga {} '.format(comDisconto5))
elif escolha == 3:
    print('Preço normal ')
elif escolha == 4:
    print('Você vai pagar 20x de juros! Com esse juros você paga {}'.format(comJuros))
else:
    print('Escolha uma das opções acima! Tente novamente ')
    
            