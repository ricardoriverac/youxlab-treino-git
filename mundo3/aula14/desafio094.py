pessoas = dict()
cadastro = list()
resp = ' '

while resp.upper() != 'N':
    pessoas['nome'] = str(input('Nome: ')).title().strip()
    pessoas['sexo'] = str(input('Sexo (M/F): ')).upper().strip()[0]
    while pessoas['sexo'] not in ('M', 'F'):
        pessoas['sexo'] = str(input('Digite M ou F para sexo: ')).upper().strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    resp = str(input('Quer continuar (S/N)?: '))
    while resp.upper() not in ('S', 'N'):
        resp = str(input('Digite S ou N: '))

print('-=' * 30)
print(f'- O grupo tem {len(cadastro)} pessoas.')

somaidade = 0
quantidade_pessoas = 0

for pessoa in cadastro:
    somaidade += pessoa['idade']
    quantidade_pessoas += 1

media = somaidade / quantidade_pessoas
print(f'- A média de idade é de {media:.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for pessoa in cadastro:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} | ', end='')
print()

print('- Lista de pessoas que estão acima da média:')
for pessoa in cadastro:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()

print('  <<< ENCERRADO >>>')