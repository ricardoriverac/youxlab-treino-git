casa= float(input('Valor da casa: '))
salario= float(input('Valor do salário: '))
anos= int(input('Anos de pagamento: '))
prestacao= casa / (anos * 12)
mensalidade= salario * (30/100)
if prestacao > mensalidade:
  print(mensalidade)
  print(f'EMPRÉSTIMO RECUSADO! Valor da prestação mensal: R${prestacao :.2f}')
else:
  print(prestacao)
  print(mensalidade)
  print(f'EMPRÉSTIMO AUTORIZADO! Prestação mensal: R${prestacao :.2f}')