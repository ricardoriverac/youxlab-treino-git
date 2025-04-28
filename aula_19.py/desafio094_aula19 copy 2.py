lista = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: ')).title().strip()
    while True:
        pessoa['sexo'] = str(input('Digite o sexo (M/F): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'Erro! por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
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
print('A lista de pessoas acima da média são: ')
for p in lista:
    if p['idade'] > media:
        print(' ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
for k, v in enumerate(lista):
    print(f'O {k+1}º cadastro tem o nome: {v["nome"]} sexo: {v["sexo"]} e idade: {v["idade"]}.')
print('finalizado')