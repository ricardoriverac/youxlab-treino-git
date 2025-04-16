# pessoa = {
#     "nome": "jao",
#     "idade": 30,
#     "cidade": "São Paulo"
# }
# pessoa['sexo'] = 'M'
# print(pessoa)
# del pessoa['idade'] #remove o elemento
# print(pessoa)
def valores_Filmes():
    filme = {
        "titulo": "Star Wars",
        "ano": 1977,
        "Diretor": "George Lucas",
    }
    print(filme.values())

def keys():
    filme = {
        "titulo": "Star Wars",
        "ano": 1977,
        "Diretor": "George Lucas",
    }
    print(filme.keys())

locadora = []
filme = {
        "titulo": "Star Wars",
        "ano": 1977,
        "Diretor": "George Lucas",
    }


estado = dict()
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil.append(estado.copy())
for estado in brasil:
    for k, i in estado.items():
        print(f'O campo {k} tem valor {i}')

    print(estado)
# filme['Personagem'] = "Darth Vader"
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# for estado in brasil:
#     print(estado)

# locadora.append(filme)
# for c, d in filme.items():
#     print(f' o {c} é {d}')
#print(filme.items()) mostra todos os itens do dicionario
# esco = str(input('O que você quer ver? T (valores) e K (keys(chaves))')).upper()
# if esco == 'T':
#     valores_Filmes()
# elif esco == 'K':
#     keys()
# base = int(input("Digite a base "))
# altura = int(input('Digite a altura: '))
# area = 0
# def calcular_Area():
#     area = base*altura
#     print(f'A area do quadrado é {area}')

    

    