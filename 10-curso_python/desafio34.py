salario = float(input('Digite um salário de um funcionário: '))
if salario >=1.250 :
    print('O seu salário com o aumento ficará: {:.3f}'.format((110/100)*salario))
else :
    print('O seu salário com aumento ficará: {:.3f}'.format((115/100)*salario))

