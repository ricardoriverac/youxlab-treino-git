num = int(input("fale um número: "))
unidade = num // 1%10 
dezena = num // 10%10
centena = num // 100%10
milhar = num // 1000%10
print(" o número {} tem ".format(num))
print("Unidade(s): {}.".format(unidade))
print("Dezena(s): {}.".format(dezena))
print("Centena(s): {}.".format(centena))
print("Milhar(es): {}.".format(milhar))
