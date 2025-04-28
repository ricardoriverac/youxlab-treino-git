estado = dict()
brasil= list()
for c  in range  (0 , 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e  in brasil:
    for k , v in e.items():
        print(f'O campo {k} tem como {v}')