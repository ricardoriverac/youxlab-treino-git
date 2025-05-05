#LISTA COMPOSTA COM ANÁLISE DE DADOS
pessoas=[]
dados=[]
cadastro=1
maior=menor=0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso:  ')))
    if len(pessoas)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    escolha=' '
    while escolha not in  'SN':
        escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha=='S':
        cadastro+=1 
    if escolha=='N':
        break
print(f'{cadastro} pessoas cadastradas.')
print(f'O maior peso é de {maior}kg. Peso de ',end=' ')
for pessoa in pessoas:
    if pessoa[1]==maior:
        print(f'{pessoa[0]}',end=' ')
print()
print(f'O menor peso é de {menor}kg. Peso de ',end=' ')
for pessoa in pessoas:
    if pessoa[1]==menor:
        print(f'{pessoa[0]}',end=' ')
print()


