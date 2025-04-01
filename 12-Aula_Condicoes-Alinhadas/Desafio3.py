num1=int(input('[Valor 1]:  '))
num2=int(input('[Valor 2]:  '))
if num1>num2:
    print('-=-'* 20)
    print('o valor 1: {} e maior que o valor 2: {}'.format(num1, num2))
    print('-=-'* 20)
elif num1<num2:
    print('-=-' *20)
    print('o valor 1: {} e menor que o valor 2: {}'.format(num1, num2))
    print('-=-' *20)
else:
    print('-=-'* 20)
    print('Numeros iguais')    
    print('-=-' *20)
        