produto = float(input('Digite o valor do produto: '))
print ("""Escolha uma das opções para pagar:
       [ 1 ] - À vista (dinheiro/cheque): 10 por cento de desconto.
       [ 2 ] - À vista no cartão: 5 por cento de desconto.
       [ 3 ] - Em até 2x no cartão: preço normal.
       [ 4 ] - 3x ou mais no cartão: 20 por cento de juros.""")
pagamento = int(input('Qual a forma de pagamento? '))
descontoAvistaDinheiro = produto * 0.9
descontoAvistaCartao = produto * 0.95
desconto2Cartao = produto
descontoMaisCartao = produto * 1.2

if pagamento == 1:
    print (f'Seu produto teve 10% de desconto! O preço atual é de R${descontoAvistaDinheiro:.2f} ')
elif pagamento == 2:
    print (f'Seu produto teve 5% de desconto! O preço atual é de R${descontoAvistaCartao:.2f} ')
elif pagamento == 3:
    print (f'O preço do seu produto permanece no valor de R$ {produto:.2f} ')
elif pagamento == 4:
    print (f'Seu produto teve um aumento de 20% de juros. Seu preço atual é de R$ {descontoMaisCartao:.2f} ')