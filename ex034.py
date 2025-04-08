salario= float(input('Informe seu salário: R$'))
if salario > 1250:
    aumento = salario * 1.10
    print('Seu salário teve um aumento de 10%, veja: R${:.2f}'.format(aumento))
if salario <= 1250:
    aumento2= salario * 1.15
    print('Seu salário teve um aumento de 15%, veja R${:.2f}'.format(aumento2))