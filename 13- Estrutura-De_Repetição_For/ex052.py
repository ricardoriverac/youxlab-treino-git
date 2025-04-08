numero = int(input("Digite um número: "))
tot =  0    
for c in range(1, numero + 1 ): 
    if numero % c == 0:
        print('\033[033m', end= '')
        tot += 1
    else:
        print('\033[031m', end='')
    print (f'{c}', c, end='')
print(f'O número {numero} foi divisível por {tot} vezes ')
