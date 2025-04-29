casa = float(input('Valor da Casa: '))

salário = float(input('Salário do comprador:'))

anos = float(input('Quantos anos vai pagar:'))

prestação = casa / (anos * 12)

minímo = salário * 30 / 100

print(f'Para pagar uma prestação de R${casa} em {anos}, a prestação será de R${prestação}')

if prestação <= minímo: 
    print('Empréstimo concedido')
else:
    print('Empréstimo negado!')