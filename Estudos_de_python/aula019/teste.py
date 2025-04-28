# dados={}
# dados={'nome':'Pedro','idade':25}
# print(dados['nome'])
# dados['peso'] = 98.5

dados = {}
dados = {'nome do filme': 'lutador ',
         'genero': 'ação',
         'nota': 87}

dados2 = {'nome do filme':'Gente Grande',
         'genero':'comedia',
         'nota': 64}

dados3 = {'nome do filme':'Eragon',
          'genero':'fantasia',
          'nota': 100}

listaFilmes = ['dados','dados2','dados3']

# print(dados.values())
# print(dados.keys())
# print(dados.items())

#for keys,values in dados.items(): 
   #print(f'O {keys} é {values}')


# estado = {}
# brasil = []

# for contador in range(0,3):
#     estado['nome'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str (input('Sigla do estado: '))
#     brasil.append(estado.copy())
# print(brasil)


brasil = []

estado1  = {'nome':'Rio de Janeiro','sigla':'Rj'}
estado2 = {'nome':'São Paulo ','sigla':'Sp'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]["sigla"])




    
