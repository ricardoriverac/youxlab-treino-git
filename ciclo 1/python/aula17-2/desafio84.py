cadastros = []
mai = men = 0
while True:
    cadastros.append([input('\nNome: '), float(input('Peso: '))][::-1])
    res = ''
    while res == '' or res[0] not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res[0] == 'N':
        break
print(f'\nCadastro(s): {len(cadastros)}.')
for m in [['Maior', max(cadastros)[0]], ['Menor', min(cadastros)[0]]]:
    print(f'\n{m[0]} peso: {m[1]}Kg. Peso de', end=' ')
    for dado in cadastros:
        if dado[0] == m[1]:
            print(f'[{dado[1]}]', end=' ')
print()