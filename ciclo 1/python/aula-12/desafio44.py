preço = float(input('Digite o preço do produto: '))
pagamento = int(input('''Escolha a condição de pagamento:
1 - À vista no dinheiro ou cheque
2 - À vista no cartão
3 - Em até 2x no cartão de debito 
4 - Em até 3x no cartão de credito '''))
if pagamento == 1:
    print('Preço final: R${:.2f}. '.format(preço-(0.10*preço)))
elif pagamento== 2:
    print('Preço final: R${:.2f}'.format(preço-(0.05*preço)))
elif pagamento== 3:
    parcelas = int(input('''Em quantas parcelas no debito?
1 - Uma (01) parcela.
2 - Duas (02) parcelas.'''))
    print('O produto custará {} parcelas de R${:.2f}. '.format(parcelas,preço/2))
elif pagamento == 4:
    parcelas = int(input('''Em quantas parcelas no crédito?
1 - Uma (01) parcela.
2 - Duas (02) parcelas.
3 - Três (03) parcelas.'''))
    print('O produto custará {} parcelas de R${:.2f}. '.format(parcelas,(preço+(0.20*preço))/parcelas))
