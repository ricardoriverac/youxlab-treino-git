km = float(input('quantos km seu carro alugado percorreu?'))
d = float(input('O carro esta alugado por quantos dias?'))
pago = (d * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))
