numeros = [[], []]
valor = 0

for c in range (1,8):
    valor = int(input('digite um número: '))
    if c % 2==0:
     numeros[0].append(c)
    else:
        numeros[1].append(c)
print(f' os números par são {sorted(numeros[0])}')
print(f' os ímpar são {sorted(numeros[1])}')