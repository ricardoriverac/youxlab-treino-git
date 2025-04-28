numero = (input('Digite um número de 0 a 9999: '))
espaco = '0000'
juncao = espaco + numero
tamanho = len(juncao)
print(f'Unidades:',juncao[tamanho-1])
print(f'Dezenas:',juncao[tamanho-2])
print(f'Centenas:',juncao[tamanho-3])
print(f'Milhar:',juncao[tamanho-4])