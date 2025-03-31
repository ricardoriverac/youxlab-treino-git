dias= int(input("Quantos dias alugado? "))
km= float(input("Quantos km rodado? "))
pago= (dias * 60) + (km * 0.15)
print("O valor cobrado vai ser R${:.2f}".format(pago))