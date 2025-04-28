n1 = int(input('Digite um número ' ))
for c in range(0, n1+1):
    print(c)
print('FIM!!')




i = int(input('Inicio '))
f = int(input('Fim '))
p = int(input('Passo '))
for v in range(i, f+1, p):
    print(v)
print('FIM')

s = 0
for o in range(0,4):
    n = int(input('Digite um número '))
    s += n
print('O Somatorio é {}'.format (s))