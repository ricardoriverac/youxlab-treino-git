soma = cont = 0
while True:
    num = int(input('Digite um número '))
    if num == 999:
        break
    cont += 1
    soma += num
print('-=-' *10)
print(f'A soma dos {cont} números é {soma}!!! ')
print('-=-' *10)
