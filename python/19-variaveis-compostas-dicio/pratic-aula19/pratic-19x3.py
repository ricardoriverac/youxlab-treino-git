estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
for c in brasil:
    for k , v in c.items():
        print(k , v)

