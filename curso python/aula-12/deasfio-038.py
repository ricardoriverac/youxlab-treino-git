num = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
if num >= num2 + 1:
    print('{} o primeiro valor é maior'.format(num))
elif num == num2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('{} segundo valor é maior'.format(num2))
