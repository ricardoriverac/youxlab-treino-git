expr = str(input('Digite a expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida.')