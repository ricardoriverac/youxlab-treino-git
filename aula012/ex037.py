num = int(input('Me diga um numero: '))
escolha =int (input(''' Escolha uma das três opções abaixo:'
[1] = binário '
[2] = octal'
[3] = hexadecimal '''))

if escolha ==1:
    print('O seu valor {} em binário e {} '.format(num,bin(num)))

elif escolha ==2:
    print('O seu valor {} em octal e {} '.format(num,oct(num)))

elif escolha ==3:
    print('O seu valor {} em hexadecimal e {} '.format(num,hex(num)))
