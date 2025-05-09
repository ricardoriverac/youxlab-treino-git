numero = 0
totalDeNumeros = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número, sendo que ao digitar 999, o programa para: '))
    if numero != 999:
        totalDeNumeros += 1 #ou totalDeNumeros = totalDeNumeros + 1
        soma += numero #ou soma = soma + numero

print ('FIM DO PROGRAMA...')
print (f'Você digitou {totalDeNumeros} números. A soma deles foi de {soma}. ')