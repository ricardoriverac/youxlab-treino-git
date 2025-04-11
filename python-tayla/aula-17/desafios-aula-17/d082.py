valores = []
par = []
impar = []

while True:
    numero = int(input('Digite um número: '))
    valores.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    pergunta = input('Quer continuar? [S/N] ').upper()

    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').upper()

    if pergunta == 'N':
        break

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')