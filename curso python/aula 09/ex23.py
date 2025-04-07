numero = int (input ("Informe um número: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar =  numero // 1000 % 10 
print("analisando o número {}".format(numero))
print ("Unidade: {}".format(unidade))
print ("Dezena: {} ".format(dezena))
print ("Centena: {}".format(centena))
print ("Milhar: {}".format(milhar))