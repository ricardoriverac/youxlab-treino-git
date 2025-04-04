nome = input('Digite o nome de uma pessoa:')
sexo = int(input(f'Fale o sexo de {nome} 1.F/2.M:'))
while sexo != 1 and 2:
    print('Tente de novo:')
    sexo = int(input((f'Fale o sexo de {nome} F/M:')))
else:
    Print('ok')


