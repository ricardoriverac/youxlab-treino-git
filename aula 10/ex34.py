salario = float (input ("Qual valor do seu salário ? R$ "))
if salario >= 1250.00:
    novo= salario + (salario * 10 / 100)
else:
      novo= salario + (salario * 15 / 100)
print("Quem ganhava {:.3f} R$ passa a receber {:.3f} R$ após o reajuste ! ".format(salario,novo))