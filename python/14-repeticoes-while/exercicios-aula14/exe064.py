cont = 0
num = 0
soma = 0 
num = int(input('Digite um número \033[31m[999]\033[m para parar: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número \033[31m[999]\033[m para parar: '))
print(f'Você digitou {cont} númeoros e a soma deles foi {soma}')