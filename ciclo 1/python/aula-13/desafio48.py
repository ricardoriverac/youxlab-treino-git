soma = 0
for i in range(1,501):
    if i % 3 == 0:
        if i % 2 == 1:
            soma += i
            print(i, end=' ')
print(f'\nA soma entre eles é {soma}', end='')
