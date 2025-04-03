s = 0
for c in range(0, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print(f'A soma dos múltiplos ímpares de três entre 1 e 500 é: {s}')