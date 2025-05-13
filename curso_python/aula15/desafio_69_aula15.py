maisDezoito = 0
homens = 0
mulheresMenosVinte = 0

while True:
    print ('CADASTRO DE PESSOAS')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
    if idade > 18:
        maisDezoito += 1
    if sexo == 'F' and idade < 20:
        mulheresMenosVinte += 1
    if sexo == 'M':
        homens += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja prosseguir? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Foram cadastradas {maisDezoito} pessoas com mais de 18 anos... ')
print (f'{homens} delas são homens... ')
print (f'E {mulheresMenosVinte} têm menos de 20 anos. ')