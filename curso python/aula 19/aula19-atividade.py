#       DICIONÁRIOS
#           { }
dados = dict ()
dados = {'Nome':'Pedro', 'idade':25}
print(dados['Nome']) # nome dentro do dicionário dados
print (dados['idade']) # idade dentro do dicionário dados
#   adicionar elementos
dados['sexo'] = 'M'
print (dados['sexo'])
#   remover elementos
del dados['idade']
#  guardar nome de filmes
filme = {'titúlo':'Star wars', 
         'ano': 1977,
         'diretor': 'George Lucas'
}
print (filme.values()) # parte de cima do dicionário
print (filme.keys()) # parte debaixo do dicionário
print (filme.items()) # pega TUDO
