salario=float(input(' Qual é seu salario: '))
if salario > 1250:
    superior = salario + (salario * 10 / 100)
    print(f'Você teve um aumento de 10%. Novo Salario R$ {superior:.2f}')

elif salario <= 1250:
    inferior = salario + (salario * 15 / 100)
    print(f'Você teve um aumento de 15%. Novo Salario R$ {inferior:.2f}')