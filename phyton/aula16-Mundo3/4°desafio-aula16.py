#ANÁLISE DE DADOS EM TUPLA
par=0
numeros=(int(input('Monte a sua tupla, digite um número: ')), int(input('Monte a sua tupla, digite um número: ')),int(input('Monte a sua tupla, digite um número: ')),int(input('Monte a sua tupla, digite um número: ')))
print(f'Sua tupla : {numeros}')
if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1}° posição')
print(f'Os valores pares digitados são os ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')

