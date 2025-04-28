dias = int(input('Quantos dias o carro foi utilizado?'))
km = float(input('Quantos km rodados?'))

pago = (dias * 60) + (km * 0.15)
print('O valor a pagar é de R${:.2f}'. format (pago))