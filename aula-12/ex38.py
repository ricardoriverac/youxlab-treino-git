n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
if n1>n2:
    print('O número {} é maior do que o número {}'.format(n1,n2))
elif n1==n2:
    print('O número {} é igual ao número {}'.format(n1,n2))
else:
    print('O número {} é maior do que o número {}'.format(n2,n1))