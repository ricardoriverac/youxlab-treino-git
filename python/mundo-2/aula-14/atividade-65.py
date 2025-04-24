print('== Analisador de Números ==')

soma = 0
quantidade = 0
maior = menor = None

while True:
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Resposta inválida. Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

media = soma / quantidade

print(f'\nVocê digitou {quantidade} números.')
print(f'A média dos valores é {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')