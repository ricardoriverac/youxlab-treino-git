lista = []
soma = quant = num = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    lista += [num]
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma/quant
print(f'Você digitou {quant} números, a média deles foi {media}\nO maior número foi '
      f'{max(lista)} e o menor {min(lista)}')
