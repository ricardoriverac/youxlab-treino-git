import pandas as pd

# carregando o dataset corretamente ==> neste caso, usa o separador ";"
# endereço ==> ./datasets/GasPricesinBrazil_2004-2019.csv
data = pd.read_csv("C:/Users/jaump/Desktop/youxlab-treino-git/curso-dados/datasets/GasPricesinBrazil_2004-2019.csv", sep=";")
print(data)

# exibe as 10 primeiras linhas do dataframe
#data.head(10)

# exibe as informações do dataset
#data.info() 

# exibe o tipo do dataframe
#type(data)

#
#data.shape

# mostra o tanto de 
#print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')