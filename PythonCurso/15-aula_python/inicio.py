cont = 1
while cont <= 10:
    print(cont, '-> ', end="")
    cont += 1
print('Acabou!! ')


n = cont = 0
while cont < 3:
    n = int(input('Digite um número '))
    cont += 1

n = s = 0
while  n != 999:
    n = int(input('Digite seu número ' ))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

