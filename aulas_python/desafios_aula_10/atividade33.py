print ('---Digite 3 números e direi qual o menor e qual o maior---')

n1 = int(input('Primeiro número? '))
n2 = int(input('Segundo número? '))
n3 = int(input('Terceiro número? '))

m = max(n1, n2, n3)
mi = min(n1, n2, n3)

print('A maior número é {}'.format(m))
print('O menor número é {}'.format(mi))