numero = (str(input('Digite um número para a posição 0 : ')),
           str(input('Digite um número para a posição 1 : ')),
           str(input('Digite um número para a posição 2 : ')),
           str(input('Digite um número para a posição 3 : ')),
           str(input('Digite um número para a posição 4 : ')))

maximo = max(numero)
minimo = min(numero)


print(F'Você digitou os valores: {numero}')
print(F'O maior valor digitado foi {maximo} na posição : {len(maximo)}')
print(F'O menor valor digitado foi {minimo} na posição : {len(minimo)}')