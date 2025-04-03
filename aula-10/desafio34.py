salario = float(input('Qual é seu salário? '))

if salario <= 1250:
    print(f'Seu aumento será de R${(salario * 0.15):.2f} totalizando R${salario * 1.15:.2f}')
else:
    print(f'Seu aumento será de R${(salario * 0.10):.2f} totalizando R${salario * 1.10:.2f}')