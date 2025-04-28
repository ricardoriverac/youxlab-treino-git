input('Diga seu nome: ')
sal=int (input('Me diga seu salario: '))
reaju =int(input('Qual reajuste deseja? '))
total= sal*reaju/100 + sal
print('Com um rejuste de {}% seu salario foi de {} para {} '.format(reaju,sal,total))

