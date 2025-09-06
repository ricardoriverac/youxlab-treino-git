num = list ()
pares = list()
impares = list()
while True:
    num.append(int(input('fale um número: ')))
    rs = str(input('quer continuar? [S/N] '))
    if rs in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('==' * 15)
print(f'a lista completa é {num}. ')
print(f'os pares são {pares}. ')
print(f'os impares são {impares}')
