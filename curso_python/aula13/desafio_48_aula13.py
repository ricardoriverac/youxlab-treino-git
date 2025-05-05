soma = 0
for n in range (0, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma = soma + n
print (f'A soma dos números ímpares múltiplos de 3 é: {soma} ') 