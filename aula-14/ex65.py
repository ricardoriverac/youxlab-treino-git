
resposta = 'S'
maiornum = 0
menornum = 0
soma = quant = media = 0

while resposta in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
media = soma / quant
print('A média entre todos foi {}'.format(media))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))


