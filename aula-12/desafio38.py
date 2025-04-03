n1 = int(input('Escolha um numero: '))
n2 = int(input('Escolha o segundo numero: '))
if n1 == n2:
    print('Não existe numero maior, os dois numeros são iguais.')
elif n1 > n2:
    print('o maior e {}'.format(n1))
else:
    print('o maior e {}'.format(n2))