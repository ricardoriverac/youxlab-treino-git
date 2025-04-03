n1=float(input("Insira seu salario "))
s= n1 +(n1*10/100)
s2 = n1 + (n1*15/100)
if n1 >= 1250:
    print("Seu salario vai ter um aumento de 10%,vai ficar:{}".format(s))
else:
    print("Seu salario vai ter um aumento de 15%,vai ficar:{}".format(s2))