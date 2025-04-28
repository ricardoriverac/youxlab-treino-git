numero = int(input('Digite um número: '))
numSeEParOuNao = numero % 2 
if numSeEParOuNao ==0 :
    print('O número {} é par. '.format(numero))
else :
    print('O número {} é ímpar. '.format(numero))
