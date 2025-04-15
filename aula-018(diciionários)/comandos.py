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
locadora.append(filme)
for c, d in filme.items():
    print(f' o {c} é {d}')
#print(filme.items()) mostra todos os itens do dicionario
# esco = str(input('O que você quer ver? T (valores) e K (keys(chaves))')).upper()
# if esco == 'T':
#     valores_Filmes()
# elif esco == 'K':
#     keys()
