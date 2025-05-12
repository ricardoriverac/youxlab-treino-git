totalDeValores = 0
soma = 0
numeros = 0

while numeros != 999:
    numeros = int(input('Digite um valor (ou 999 para parar) : '))
    if numeros == 999:
        break
    soma += numeros
    totalDeValores += 1
print (f'A soma dos {totalDeValores} valores é de {soma}! ')