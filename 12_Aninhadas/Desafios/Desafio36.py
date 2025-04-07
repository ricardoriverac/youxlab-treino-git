n1 = float(input("Insira o valor da casa: "))
n2 = float(input("Insira seu salario: "))
n3 = int(input("Quantos anos voce ira pagar: "))
p = n2 * 30 / 100 
a = n1 / (n3*12)
print("Para pagar uma casa de {:.2f},em {}anos".format(n1,n3))
print("A prestação vai ficar {:.1f},".format(a))
if p <= a:
    print("Seu emprestimo foi aprovado: ")
else:
    print("Seu emprestimo foi negado: ")

