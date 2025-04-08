resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('digite um número: '))
    soma += num
    quant += 1

    resp = str(input('quer continuar? [S/N]')).upper().strip()[0]
print('terminou')
