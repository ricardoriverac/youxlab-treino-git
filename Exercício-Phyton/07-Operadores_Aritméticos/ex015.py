dias = int(input('Quantos dias alugados? '))
km = float(input('Qunatos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(' O total a pagar é de R${}'.format(pago))