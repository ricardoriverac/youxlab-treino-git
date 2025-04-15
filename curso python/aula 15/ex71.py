print ("\t-----" * 4)
print ("<<<<<<<<<<<<<<< CAIXA ELETRÔNICO >>>>>>>>>>>>>>>")
print ("\t-----" * 4)
saque = int (input ("Qual valor do saque ? "))
cedula50 = cedula20 = cedula10 = cedula5 = cedula1 = 0
while saque >= 50:
    saque -= 50
    cedula50 += 1
while saque >= 20:
    saque -= 20
    cedula20 += 1
while saque >= 10:
    saque -= 10
    cedula10 += 1
while saque >= 5:
    saque -= 5
    cedula5 += 1
while saque >= 1:
    saque -= 1
    cedula1 += 1
while saque < 0:
    break
print ("\t-----" * 4)
print (f"Quantidade de cédulas de 50 reais: {cedula50}")
print ("\t-----" * 4)
print (f"Quantidade de cédulas de 20 reais: {cedula20}")
print ("\t-----" * 4)
print (f"Quantidade de cédulas de 10 reais: {cedula10}")
print ("\t-----" * 4)
print (f"Quantidade de cédulas de 5 reais: {cedula5}")
print ("\t-----" * 4)
print (f"Quantidade de cédulas de 1 reais: {cedula1}")
print ("\t-----" * 4)




