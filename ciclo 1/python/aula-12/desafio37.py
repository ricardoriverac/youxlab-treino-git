from time import sleep
n = int(input('Digite um número para conversão: '))
n2 = int(input('Digite 1 para binário\nDigite 2 para octal\nDigite 3 para hexadecimal: '))
print('CONVERSÃO EM ANDAMENTO...')
sleep(3)
if n2 == 1:
    print(bin(n))
elif n2 == 2:
    print(oct(n))
elif n2 == 3:
    print(hex(n))
