import uteis

numero = int(input('Digite um número: '))
fat = uteis.fatorial(numero)
print(f'O fatorial de {numero} é {fat}')
print(f'O dobro de {numero} é {uteis.dobro(numero)}')
print(f'O triplo de {numero} é {uteis.triplo(numero)}')