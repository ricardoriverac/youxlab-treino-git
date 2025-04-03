valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite mais um número: '))
valor3 = int(input('Digite outro número: '))
valor4 = int(input('Digite o ultimo: '))
tupla = (valor1 , valor2 , valor3 , valor4 )
print(f'O valor 9 apareceu apenas {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3)+1}°')
else:    
    print('O valor 3 foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in tupla :
    if n % 2 == 0:
        print(n, end=' ')