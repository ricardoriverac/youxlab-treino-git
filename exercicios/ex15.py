dias = int (input ("quantos dias você alugou esse carro ?  "))
km = float (input ("quantos km você andou ?  "))
pago = (dias * 60 ) + (km * 0.15)
print ("O total a pagar é de {:.2f} R$".format(pago))