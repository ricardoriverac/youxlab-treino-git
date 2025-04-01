salario = float(input('Qual o valor do seu salário '))

salario_maior = salario + (salario * 10 / 100)
salario_menor = salario + (salario * 15 / 100)

if salario > 1250:
    print('Você tera R${:.2f}, de salário'.format(salario_maior))
else:
    print('Você tera R${:.2f}, de salário'.format(salario_menor))

