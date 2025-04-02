from time import sleep
primeiroValor = int(input('Digite um número: '))
segundoValor = int(input('Digite outro: '))
osDoisJuntos = (primeiroValor, segundoValor)
print('VERIFICANDO QUAL VALOR É MAIOR...')
sleep (2)
if primeiroValor>segundoValor :
    print ('O primeiro valor, cujo é {}, é maior.'.format(primeiroValor))
elif segundoValor>primeiroValor :
    print('O segundo valor, cujo é {}, é maior.'.format(segundoValor))
elif primeiroValor==segundoValor:
    print('Não existe um número maior, os dois valores são iguais.')
