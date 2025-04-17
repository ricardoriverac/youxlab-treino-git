#mostrando uma informação expecifica
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

#mostrando só as keys
print(pessoas.keys())

# #values
print(pessoas.values())

#items
print(pessoas.items()) #coloca os itens em uma lista e dentro da lista coloca tuplas

#usando for
for k in pessoas.keys(): #mostra só o titulo do dicionario
    print(k)

for v in pessoas.values(): #mostra oq ta dentro das keys
    print(v)

for k, v in pessoas.items(): #mostra keys e values ao msm tempo
    print(f'{k} = {v}')

#trocando a informação
pessoas['nome'] = 'Leandro'
print(pessoas)

#adicionando elemento
pessoas['peso'] = 98.5
print(pessoas)

# #colocando dicionarios dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

# #mostrando a lista
print(brasil) #mostra a lista completa
print(brasil[0]) #mostra 'estado 1'
print(brasil[1]) #mostra 'estado 2'
print(brasil[1]['sigla']) #mostra só a silga do estado 2

#fazendo copia de um dicionario
estado = {}
brasil = []
for c in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy()) #COPY faz a copia do dicionario
print(brasil)

for e in brasil: #só pra deixar bonito
    for v in e.values():
        print(v, end=' ')
    print()