salario = int(input('Digite o valor do salário: '))
aumento15 = salario * 0.15
aumento10 = salario * 0.1
if salario <= 1250:
    print (f'O salário com 15% de aumento é de R$ {salario + aumento15} ')
elif salario >= 1250:
    print (f'O salário com 10% de aumento é de R$ {salario + aumento10} ')