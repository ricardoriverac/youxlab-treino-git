import pandas as pd
data = pd.read_csv('aulas_dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(10))
print(data.info())