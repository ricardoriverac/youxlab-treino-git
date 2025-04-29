estado = dict()
brasil = list()
escolha = 'S'

while escolha != 'N':
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    escolha = str(input('Quer continuar? [S/N]')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'Não temos a opção {escolha}\n[S/N]')).upper()
for e in brasil:
    for v in e.items():
        print(v, end=' ')
    print()