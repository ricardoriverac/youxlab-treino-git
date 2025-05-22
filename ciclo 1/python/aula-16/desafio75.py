numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
numero4 = int(input('Digite o último número: '))

numeros = (numero1, numero2, numero3, numero4)
quantidadePares = 0

print(f'\nVocê digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

# verificar se o número 3 foi digitado
if numeros.count(3) > 0:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado nenhuma vez')

# imprimir os valores pares
print(f'Os valores pares digitados foram: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
        quantidadePares += 1

# verificar se foi digitado algum número par
if quantidadePares == 0:
    print('Nenhum número par foi digitado.')
print()