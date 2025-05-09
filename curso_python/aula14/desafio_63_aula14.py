elemento = int(input('Quantos elementos da sequência de Fibonacci deseja ver? '))

primeiroElemento = 0
segundoElemento = 1
sequencia = ''

if elemento == 1:
    print (f'{primeiroElemento} -> ' ,end='')
else:
    print (f'{primeiroElemento} -> {segundoElemento} -> ' ,end='')

contador = 3
while elemento >= contador:
    terceiroElemento = primeiroElemento + segundoElemento
    print (f'{terceiroElemento} ->' ,end='')
    primeiroElemento = segundoElemento
    segundoElemento = terceiroElemento
    contador += 1

print ('Fim')