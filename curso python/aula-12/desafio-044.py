valor = float(input('Qual o valor do produto?'))
vezes = int(input('Em quantas vezes você quer dividir?'))
print('Formas de pagamento: \n 1.A vista (Dinheriro/cheque) \n 2. A vista no cartão \n 3.Em até 2x no cartão \n 4.3x ou mais')
formapagamento = int(input('Qual a forma de pagamento?'))
desconto = valor - (valor * 0.1)
descontocart = valor - (valor * 0.05)
parcela = valor / 2
juros = valor * 0.2
j = valor + juros

if formapagamento == 1:
    print('Aplicamos um desconto de 10%, o valor total ficará em:')
    print(desconto)
if formapagamento == 2:
    print('Aplicamos um desconto de 5"%" o valor total ficará em:')
    print(descontocart) 
if formapagamento == 3:
    print('O valor das parcelas em 2x no cartão ficará em:')
    print('R${} por mês'.format(parcela))
if formapagamento == 4:
    print('O valor terá 20"%" de juros')
    print('O valor total com um juros de 20"%" aplicado fica em R${}'.format(j))
