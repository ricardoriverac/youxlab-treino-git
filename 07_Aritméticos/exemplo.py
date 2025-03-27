n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2 
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
print("A soma e {},\n A multiplicação e {}\n A divisao e{:.3f}".format(s,m,d))
print("A potencia e{}, \n Divisao inteira e{}\n ".format(p,di))
