import pandas as pd

# Carregando o dataset corretamente, que usa o separador(sep) usando ;
data = pd.read_csv('dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
# print(data)

# Exibe as 5 primeiras linhas, mas da pra mudar a quantidade de linhas pelos ()
# print(data.head())

# Mostra algumas informações sobre os dados
# data.info() 


# Data Frame

# Mostra o tipo dos dados
# print(type(data))

# Mostra uma tupla com a forma do Dataset
# print(data.shape)
# Ex: 
# print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis')

# Criando um DataFrame
personagens_df = pd.DataFrame({
    'nome' : ['Luke Skyewalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70.5, 15.2, 60.1],
    'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
})
# print(personagens_df)

# Renomeando colunas de um DataFrame
# DataFrame.columns retorna uma lista com o nome todas as colunas de um DataFrame

# print(personagens_df.columns)

# print(type(personagens_df.columns))

# Para renomear uma coluna de um DataFrame, podemos utilizar o método DataFrame.rename que retorna uma cópia com as alterações

# personagens_df_renomeado = personagens_df.rename(columns={
#     'eh jedi' : 'É jedi',
#     'idade' : 'Idade',
#     'peso' : 'Peso'
# })
# print(personagens_df_renomeado)


# Para renomear sem ser em uma cópia usamos o inplace=True no final

# personagens_df.rename(columns={
#     'eh jedi' : 'É jedi',
#     'idade' : 'Idade',
#     'peso' : 'Peso'
# }, inplace=True)
# print(personagens_df)

# Uma outra forma de renomear todas as listas de um data frame é passar uma lista com os novos nomes de uma colunas para o atributo DataFrame.columns

# personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH_JEDI']
# print(personagens_df)


# Series

# Selecionando uma coluna inteira (é como selecionar um dicionário no python)

# personagens_df['NOME']

# Selecionando uma coluna inteira
# esta forma de acesso, só funciona para colunas sem espaços, acentos, etc (caracteres inválidos)
# personagens_df.NOME (NÃO RECOMENDADO)

# Selecionando a observação indexada no índice [1] do dataframe
# print(data.iloc[1])

# print(type(data.iloc[1]))

# Criando uma series
seriesUm = pd.Series([1, 2.5, 10.5], index=['Prova 1', 'Prova 2', 'Projeto'], name='Notas do Yuri')
# print(seriesUm)
# O index serve para adicionar nome nos índices e o name serve para colocar um nome na Series
