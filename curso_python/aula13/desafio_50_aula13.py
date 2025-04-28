soma = 0
for n in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    pares = numero % 2 == 0
    if pares:
        soma += numero
print (f'A soma dos números pares é de {soma}')