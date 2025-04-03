print('===' *20)
print('LOJÁ DO CRUZEIRO ESPORTE CLUBLE')
print('===' *20)

print('-=-='*20)

print(''' FORMA DE PAGAMENTO
      [ 1 ] Á vista dinheiro/cheque 10% de desconto!!
      [ 2 ] Á vista cartão 5% de desconto!!
      [ 3 ] 2x cartão
      [ 4 ] 3x ou mais no cartão, 20% juros!! ''')
valor = float(input('Qual o valor do produto?? '))

opção = int(input('Qual vai ser a opção?? '))

if opção == 1:
    total = valor - (valor * 10 / 100)
    print('Você ganhou 10% de desconto, o valor agora é de R${:.2f}'.format(total))

elif opção == 2:
    total = valor - (valor * 5 / 100)
    print('Você ganhou 5% de desconto, o valor agora é {}'.format(total))

elif opção == 3:
    total = valor / 2
    print('O seu produto fiocu em 2 parcelas de R${}'.format(total))

elif opção == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Em Quantas parcelas?? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x, de R${}.'.format(totparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!!'.format(valor, total))


