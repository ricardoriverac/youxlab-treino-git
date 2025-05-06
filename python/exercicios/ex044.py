produto= float(input('Valor do produto:R$'))
condicaoDePagamento= int(input('Condições de Pagamento: \n 1 para dinheiro ou cartão á vista \n 2 para no cartão á vista \n 3 para até 2x no cartão \n 4 para 3x ou mais no cartão \n Escolha uma condição: '))
if condicaoDePagamento == 1:
    calculo1= produto * (10/100)
    print('Você ganhou 10% de desconto. Valor atual do produto:R${:.2f}'.format(calculo1))
elif condicaoDePagamento == 2:
    calculo2= produto * (5/10)
    print('Você ganhou 5% de desconto. Valor atual do produto:R${:.2f}'.format(calculo2))
elif condicaoDePagamento == 3:
    print('Valor normal do produto: {:.2f}'.format(produto))
elif condicaoDePagamento == 4:
    calculo3= produto * (20/10)
    print('Valor do produto dividido em 3x ou mais com 20% de juros {:.2f}'.format(calculo3))
