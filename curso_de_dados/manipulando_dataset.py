import pandas as pd
data = pd.read_csv('./curso_Dados-Pandas/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data)
print(data.head()) # retorna as linhas do dataset e pode ser determinado o tanto que quer ver
# print(data.info()) retorna as informações detalhadas sobre
print(f'O Dataframe possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variaveis')
nrows, ncols = data.shape
nrows, ncols
novos_produtos = [f'Produtos {i}' for i in range(nrows)]
len(novos_produtos)