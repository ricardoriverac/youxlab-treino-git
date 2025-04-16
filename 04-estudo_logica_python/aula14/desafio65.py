numeros = 0
menor = 0
maior = 0
soma = 0
r = 's'
while r in 'Ss':
    numero = int(input('Digite um número: '))
    if menor == 0:
        menor = numero
    if menor > numero:
        menor = numero
    if maior < numero:
        maior = numero
    numeros += 1
    soma += numero
    r = str(input('Deseja continuar? [S/N]: ')).upper()
print(f'A média entre os {numeros} números digitados é {soma/numeros}')
print(f'o maior valor digitado é {maior} e o menor valor digitado é {menor}.')