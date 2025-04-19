dados = list()
dados.append(['Pedro', 'Ana', 'Iza'])
dados.append([25, 21, 19])
print(dados)
dados = {'nome': dados[0], 'idade': dados[1]}
print(dados['nome'])
print(dados['idade'])

filme = {'nome': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'}
print(filme['ano'])
print(filme.values()) #mostrar os nomes
print(filme.keys()) #mostrar as chaves
print(filme.items()) #mostrar tudo
for k,v in filme.items():
    print(f'O {k} é {v}')
locadora = list()
locadora.append(filme)
locadora.append({'nome': 'Avengers',
                 'ano': 2012,
                 'diretor': 'Joss Whedon'})
print(locadora[0]['ano'])
print(locadora[1]['ano'])