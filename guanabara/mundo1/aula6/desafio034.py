salario = float(input('qual é o salário do funcionário? '))
if salario >= 1250:
    aumento1 = salario * 10/100
    resultado1 = salario + aumento1
    print(f'o funcionário que ganhava {salario} passará a receber {resultado1}')
else:
    aumento2 = salario * 15/100
    resultado2 = salario + aumento2
    print(f'o funcionario que ganhava {salario} passará a receber {resultado2}')
