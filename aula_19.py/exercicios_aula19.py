pessoas={'nome':'Gustavo', 'sexo': 'masculino', 'idade':22}
print(pessoas.items())

pessoas={'nome':'Gustavo', 'sexo': 'masculino', 'idade':22}
del pessoas ['sexo']
for k, v in pessoas.items():
    print(f'{k}= {v}')


brasil = []
estadol = f'uf':'Rio de janeiro', 'sigla': 'RJ')
estado2= f'uf': 'São Paulo', 'siala': 'SP']
brasil.append(estadol)
brasil.append(estado2)
print(estado2)

estado = dict()
brasil = list()
for c in range(0, 3):
        estado['uf'] = str(input('Unidade Eederatixa:'))
        estado['sigla'] = str(input('Sigla do Estado:'))
brasil.append(estado.copy())
for e in brasil:
  for k, v in e.items():
       print(v, end='')
  print()