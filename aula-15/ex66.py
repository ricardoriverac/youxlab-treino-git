soma = cont = num = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
soma -= 999
cont -= 1
print(f'A soma de todos os {cont} números, é igual a: {soma}')
