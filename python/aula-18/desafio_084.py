pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ').strip().capitalize()))
    dados.append(int(input('Digite seu peso: ')))
    if not pessoas:
        maior = menor = dados[1]
    pessoas.append(dados[:])
    for valor in pessoas:
        if valor[1] > maior:
            maior = valor[1]
        elif valor[1] < menor:
            menor = valor[1]
    dados.clear()
    resp = ''
    while not resp or resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if not resp or resp not in 'SsNn':
            print('Opção inválida!')
        else:
            break
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso registrado foi: {maior}Kg.')
print(f'As pessoas mais pesadas foram:', end=' ')
for valor in pessoas:
    if valor[1] >= maior:
        print(valor[0], end='. ')
print(f'\nO menor peso registrado foi: {menor}Kg.')
print(f'As pessoas mais leves foram:', end=' ')
for valor in pessoas:
    if valor[1] <= menor:
        print(valor[0], end='. ')