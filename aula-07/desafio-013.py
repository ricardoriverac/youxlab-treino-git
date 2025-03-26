salario = float(input('Qual seu salario?'))
nsalario = salario + (salario*15 / 100)


print('seu salario era R${:.2f} e terá um aumento de 15 porcento então ficará R${:.2f}'.format(salario, nsalario))
