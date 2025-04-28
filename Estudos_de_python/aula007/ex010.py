valor = int (input('Me diga o valor em reais ou dolar que deseja converter:R$ '))
dolar = valor/5.50
real = valor*5.50

print('Se R${} for em reais você tera R${:.3f} dolares, mas se for em dólares você tera R${} reais '.format(valor,dolar,real))

