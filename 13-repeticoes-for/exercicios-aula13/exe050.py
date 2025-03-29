soma = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0 :
        soma += n
print(f'a soma de todos pares será {soma}')