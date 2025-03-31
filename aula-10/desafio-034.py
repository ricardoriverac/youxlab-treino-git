salario = float(input('Digite seu salário:'))
r = (salario * 1.10) - salario
s = (salario * 0.15) + salario


if salario >= 1250:
    print('O valor do seu salário aumentou em 10% valor total: R${:.2f}'.format(salario * 1.10))
    print('valor dos 10%: R${:.2f}'.format(r))
else:
    print('O valor do seu salário aumentou em 15% valor total: R${}'.format(s))
    print('Valor dos 15%: R${}'.format(salario * 0.15))