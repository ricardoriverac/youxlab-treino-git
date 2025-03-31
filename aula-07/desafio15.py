dias = int(input("Quantos dias você ficou com o carro?"))
km = float(input('Quantos quilomêtros você percorreu com o carro?'))

valor = (dias * 60 ) + (km * 0.15)

print('O valor do aluguel do carro por {} dias foi de:\nR${:.2f}'.format(dias, valor))