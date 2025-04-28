salario = float(input('Qual é o seu salário? R$'))
aumento1 = salario * 0.10
aumento2 = salario * 0.15
if salario > 1250:
    print(f'Parabéns você recebeu 10% de aumento. Seu novo salário é de R${aumento1 + salario:.3f}')
if salario < 1250:
    print(f'Parabéns você recebeu 15% de aumento. Seu novo salário é de {aumento2 + salario:.3f}')