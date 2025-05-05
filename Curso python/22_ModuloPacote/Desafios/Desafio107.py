def dobro(a):
	return print(f"O dobro de {a} é R${a * 2}R$ ")
def metade(a):
	return print(f"A metade de {a} é R${a / 2} ")
def aumentar(a):
	b = a * 10/100
	return print(f"{a} Aumentando em 10%, temos R${b + a}")
n = float(input("Digite o preço: R$ "))
metade(n)
dobro(n)
aumentar(n)