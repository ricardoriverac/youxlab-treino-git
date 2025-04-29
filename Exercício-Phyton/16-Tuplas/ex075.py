nove = 9
cont = 0
pares = []

numero = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o ultimo número: ')))

if numero == nove:
    cont += 1

print(f'Você digitou os valores : {numero}')

print(f'O número nove aparece {numero.count(9)} vezes')

print(f'O número 3 foi digitado pela primeira vez na {numero.index(3)+1} posição' if 3 in numero else 'Não foi digitado número 3') 

print('Os valores pares são:', {n for n in numero if n % 2 == 0}, end=' ')
