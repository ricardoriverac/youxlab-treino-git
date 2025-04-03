a1 = int(input('Digite um número: '))
d = int(input('Qual é a razão da PA? '))
n = 11
an = a1 + (n-1)*d
for termo in range(a1, an, d):
    print(termo)
