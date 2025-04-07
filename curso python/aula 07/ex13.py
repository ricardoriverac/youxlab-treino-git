salario = float (input ("Digite seu salário : R$"))
reajuste = salario + (salario* 15/ 100)
print ("Uma pessoa que ganha {:.2f}RS, com um reajuste de 15% passa a receber {:.2f}R$".format(salario,reajuste))