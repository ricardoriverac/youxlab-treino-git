cont = 0
soma = 0
while True:
    num = int(input('Digite varrios números:'))
    if num == 999:
        break

    cont += 1
    soma = soma + num
print(f'{cont} foram digitados.')
print(f'A soma desses números foi {soma}')
        