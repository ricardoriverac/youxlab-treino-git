lista = []
pessoas = {}
soma = media = 0
while True:
    pessoas['nome'] = str(input('Digite o nome: ')).title().strip()
    while True:
        pessoas['sexo'] = str(input('Digite o sexo (M/F): ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print(f' Por favor digite apenas M ou F.')
    pessoas['Idade'] = int(input('Digite a idade: '))
    soma += pessoas['Idade']
    lista.append(pessoas.copy())
    while True:
        perg = str(input('Deseja continuar (S/N): ')).upper()[0]
        if perg in 'SN':
            break
        print(f'Erro! Responda apenas S ou N.')
    if perg == 'N':
        break
print(lista)
print()
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
media = soma / len(lista)
print(f'A média de idade é {media:.2f} anos.')
print(f'As mulheres cadastradas foram:', end=' ')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('A lista de pessoas acima na média são: ')
for p in lista:
    if p['Idade'] > media:
        print(' ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
for k, v in enumerate(lista):
    print(f'O {k+1}º cadastro tem o nome: {v["nome"]} sexo: {v["sexo"]} e idade: {v["Idade"]}.')
