numero = int (input(" Digite um número para ver sua tabuada: "))
print ("\t_=_" * 10)
for c in range(0,11):
     print ("\033[32m{}\033[m x \033[32m{}\033[m = \033[34m{}\033[m".format(numero, c , numero*c))