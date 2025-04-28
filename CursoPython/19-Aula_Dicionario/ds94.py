galera = list()
pessoa = dict()
soma_idade = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break
print('=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma_idade / len(galera)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres  cadastrads  foram ', end=' ')
for p  in galera:
    if p["sexo"] in 'Ff':
        print(f' {p["nome"]} ', end=' ')
print()
print('D) Listas das pessoas que estão acima da media:  ')
for p  in galera:
    if p['idade'] >= media:
        print('   ' , end = ' ')
        for k , v in p.items():
            print(f' {k} = {v}: ', end='')
        print()
print('>>>>>>><<<<<<<<')