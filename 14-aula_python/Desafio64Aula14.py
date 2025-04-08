num =cont =soma = 0
num = int(input('Digite um número [999 para parar ]: '))
while num != 999:
    num = int(input('Digite um número [999 para parar ]: '))
    cont += 1
    soma += num
print('Soma {}'.format(cont))