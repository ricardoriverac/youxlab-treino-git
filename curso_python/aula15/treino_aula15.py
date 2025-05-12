numero = soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print (f'A soma vale {soma}. ')