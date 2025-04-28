s = 0
for n in range(0, 6):
    n = int(input('Digite um número: '))
    par = n % 2
    if par == 0:
        s += n
print(f'A soma dos números pares é {s}')