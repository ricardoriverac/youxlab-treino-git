pessoas = {'Nome': 'Gustavo', 'Sexo': 'Masculino', 'Idade': '22'}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
# del pessoas['Sexo']
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = '98.5'
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print (v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
Brasil = []
estadoUm = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ' }
estadoDois = {'uf': 'São Paulo', 'Sigla': 'SP' }
Brasil.append(estadoUm)
Brasil.append(estadoDois)
print(Brasil[1]['Sigla'])

estado = {}
brasil = []
for c in range (0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['Sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items(): 
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()