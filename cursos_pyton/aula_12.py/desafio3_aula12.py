numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite mais um número inteiro: '))
if numero1 > numero2:
    print('O número {} é maior do que o número {}.'.format(numero1, numero2))
elif numero1 < numero2:
    print('O número {} é maior do que o número {}.'.format(numero2, numero1))
else:
    print('Os dois valores são iguais. Valores digitados: {}.'.format(numero1))