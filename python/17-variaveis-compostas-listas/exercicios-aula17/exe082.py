valores = []
par = []
impar = []
while True:
    numero = int(input('Digite um número: '))
    valores.append(numero)
    if numero % 2 == 0 :
        par.append(numero)
    if numero % 2 == 1 :
        impar.append(numero)
    sair = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')