salario = float(input('Qual o seu salario atua: '))
if salario >= 1250:
  aumento1 = salario * 10/100
  atual = salario + aumento1
  print(f'Seu salario era R${salario} e agora sera de R${atual}')
else:
  aumento2 = salario * 15/100
  resultado = salario + aumento2
print(f'Seu salario era de R${salario} e agora sera R${resultado}')