n = input('Digite um numero de 0 a 9999: ')
s = '000' + n
print(f'Unidade {s[-1]}')
print(f'Dezena {s[-2]}')
print(f'Centena {s[-3]}')
print(f'Milhar {s[-4]}')