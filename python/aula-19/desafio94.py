dicio = {}
pessoas = []
média = 0
while True:
    dicio['Nome'] = str(input('\nNome: ')).strip().title()
    dicio['Idade'] = int(input('Idade:'))
    dicio['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while dicio['Sexo'] != 'M' and dicio['Sexo'] != 'F':
        dicio['Sexo'] = str(input('Decisão inválida! Sexo: [M/F]')).upper()[0]
    pessoas.append(dicio.copy())
    decisão = str(input('Deseja continunar o cadastro? [S/N] ')).upper()[0]
    while decisão != 'S' and decisão != 'N':
        decisão = str(input('Decisão inválida! Deseja continuar o cadastro? [S/N] ')).upper()[0]
    if decisão in 'Nn':
        break
print(f'\nA) O total de pessoas cadastradas foram {len(pessoas)}.')
print(f'B) A média das idades são {média/len(pessoas):.2f}.')
print('C) As mulheres cadastradas foram ', end='')
for v in range(0, len(pessoas)):
    média += pessoas[v]['Idade']
    if pessoas[v]['Sexo'] == 'F':
        print(f'{pessoas[v]["Nome"]}', end=' ')
print()
print('D) A lista de pessoas com idade acima da média:')
for v in range(0, len(pessoas)):
    if pessoas[v]['Idade'] >= média/len(pessoas):
        print(f'   Nome: {pessoas[v]["Nome"]}, Idade: {pessoas[v]["Idade"]}, Sexo: {pessoas[v]["Sexo"]}')
print()