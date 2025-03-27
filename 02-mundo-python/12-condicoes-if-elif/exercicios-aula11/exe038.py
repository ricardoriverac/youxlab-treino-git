a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b :
    print('\033[1;35mo PRIMEIRO valor é maior\033[m')
elif b > a :
    print('\033[1;35mO SEGUNDO valor é maior\033[m')
elif a == b :
    print('\033[1;35mOs valores são iguais\033[m')    
