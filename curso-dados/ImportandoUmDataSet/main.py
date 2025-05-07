import pandas as pd

# # carregando o dataset corretamente ==> neste caso, usa o separador ";"
data = pd.read_csv("C:/Users/jaump/Desktop/youxlab-treino-git/curso-dados/datasets/GasPricesinBrazil_2004-2019.csv", sep=";")
print(data)

# exibe as 10 primeiras linhas do dataframe
data.head(10)