soma = 0
cont = 0
for x in range(1, 7):
    n = int(input('Digite o {}° numero: '.format(x)))
    if n % 2 == 0:
        soma += n
        cont+= 1

print(soma)