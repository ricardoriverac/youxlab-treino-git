print('Tabela de gastos:')
print('1.Fast Food')
print('2.Shopee')
print('3.Contas')
print('4.Reserva')
t = int(input('Para onde foi o valor gasto?'))
if t == 1:
    v1 = float(input('Qual foi o valor?'))
    print('Você gastou R${} com fast food'.format(v1))
    