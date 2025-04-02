n1 = int(input("Insira um numero: "))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print("Analisando o numero {}".format(n1))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print('Centena: {}'.format(c))
print("Milhar: {}".format(m))
