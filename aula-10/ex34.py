salario=float(input('Qual o valor do salário? '))
if salario>1250:
    aumento=10/100
    salarioaumento=salario+(salario*aumento)
    print('Seu sálario com o aumento de dez porcento será de R${}'.format(salarioaumento))
else: 
    aumento=15/100
    salarioaumento=salario+(salario*aumento)
    print('Seu salario com o aumento de quinze porcento será de R${}'.format(salarioaumento))