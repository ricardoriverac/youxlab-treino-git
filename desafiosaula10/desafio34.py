salario = float(input('Digite seu salário: '))
aumentoSuperiorPorcentagem = 110/100
aumentoInferiorPorcentagem = 115/100
aumentoSuperior = salario * aumentoSuperiorPorcentagem
if salario > 1250:
    print('Você tem direito á um aumento de 10%, com esse aumento seu salário fica {:.2f}'.format(salario * aumentoSuperiorPorcentagem))
else:
    print ('Seu salário tem direito á um aumento de 15%, com esse aumento seu salário fica {:.2f}'.format(salario * aumentoInferiorPorcentagem))
