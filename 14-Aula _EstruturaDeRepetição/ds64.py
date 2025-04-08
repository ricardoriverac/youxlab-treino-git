num =cont =soma = 0
num = int(input('Digite um numero [999 para parar ]: '))
while num != 999:
    num = int(input('Digite um numero [999 para parar ]: '))
    cont += 1
    soma += num
print('Soma {}'.format(num))