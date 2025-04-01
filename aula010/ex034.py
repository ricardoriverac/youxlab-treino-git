sal=int(input('Digite seu salário: '))
novosal = (sal*15)/100 + sal
if sal <= 1550:
    print('Seu novo salario sera de: {} '.format(novosal))
else:
    print('Seu novo salario sera de: {} '.format(sal*5)/100 + sal)