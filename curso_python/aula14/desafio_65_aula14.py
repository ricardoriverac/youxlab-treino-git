totalDeNumeros = 0
soma = 0
menor = 0
maior = 0
maisNumeros = 'S'

while maisNumeros in 'S':
    numero = int(input('Digite um valor: '))
    totalDeNumeros += 1
    soma += numero
    if totalDeNumeros == 1:
        menor = maior = numero #se houver apenas 1 valor, ele é o maior e o menor número.
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    maisNumeros = str(input('Quer digitar mais valores? [S/N] ')).upper()

print (f'Você digitou {totalDeNumeros} e a média foi de {soma/numero}')
print (f'O maior número foi {maior} e o menor foi {menor}. ')