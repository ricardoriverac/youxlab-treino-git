# cont = 1
while cont <= 10:
    print(cont, '--> ', end=' ')
    cont += 1
print('Acabou')

#usando o true - deixa em loop infinito
cont = 1
while True:
    print(cont, '--> ', end=' ')
    cont += 1
print('Acabou')

#usando o break pra parar o loop e somando os valores
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')