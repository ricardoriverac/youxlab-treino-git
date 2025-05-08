import pandas as pd
data = pd.read_csv('aulas_dados/datasets/venda-de-carros.csv', sep=';')
print(data)
data.head()
data.info()
print(type(data))
data.shape
print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis. ')
personagens_df = pd.DataFrame({
    "nome": ['Nagi', 'Isagi', 'Bachira'],
    "idade": ['17', '18', '18'],
    "peso": ['78.9', '75.7', '70.4'],
    "eh jedi": [False, False, False]
})
print(personagens_df.info())
print(personagens_df.columns)
print(type(personagens_df.columns))
print(list(personagens_df.columns))
personagens_df_Renomeado = personagens_df.rename(columns={
    'nome': 'Nome Completo',
    'idade': 'Idade'
})
print(personagens_df_Renomeado)
personagens_df.columns= ['NOME', 'IDADE', 'PESO', "EH JEDI"]
print(personagens_df)
print(data.columns)
print(type(data.iloc[1]))
# produtoCopyBK = data['PRODUTO'].copy()
# print(produtoCopyBK)
# data['PRODUTO'] = 'Combustível'
# print(data.head())
# print(data['Fabricante'].view)
