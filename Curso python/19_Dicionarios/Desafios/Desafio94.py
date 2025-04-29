pessoal = list()

pessoa = dict()

mulheres = list()

m = list()

soma = 0

while True:

    pessoa['nome'] = str(input('NOME:'))

    pessoa['sexo'] = str(input('SEXO:[F/M]')).upper().strip()

    while pessoa['sexo'] not in 'FM':

        print('ERRO...Digite apenas F ou M')

        pessoa['sexo'] = str(input('SEXO:[F/M]')).upper().strip()

    pessoa['idade'] = int(input('IDADE:'))

    pessoal.append(pessoa.copy())

    continuar = str(input('QUER CONTINUAR?[S/N]')).upper().strip()

    if continuar in 'N':

        break

    while continuar not in 'SN':

        print('ERRO...Digite apenas S e N')

        continuar = str(input('QUER CONTINUAR?[S/N]')).upper().strip()

print(f'FORAM CADASTRADAS {len(pessoal)} PESSOAS')

for dicio in pessoal:

    soma += dicio['idade']

    if dicio['sexo'] in 'F':

        mulheres.append(dicio['nome'])

    if dicio['idade'] > soma/len(pessoal):

        m.append(dicio['idade'])

print(f'A MÉDIA DAS IDADES É:{soma/len(pessoal)}')

print(f'AS MULHERES CADASTRADAS FORAM:{mulheres}')

print(F'AS IDADES ACIMA DA MÉDIA FORAM: {m}')