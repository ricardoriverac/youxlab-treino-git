soma = 0
cont = 0
while True:
    n = int(input('Digite o número \033[31m[999]\033[m para parar: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números é a soma deles foi {soma}')