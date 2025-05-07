import pandas as pd
data = pd.read_csv('./curso_dados/datasets/GasPricesinBrazil_2004-2019 (1).csv')
print(data.head())
idades = pd.Series([45, 23, 17, 59], index = ['Gilmar', 'Larissa', 'Ana Clara', 'José Maria'])
print(idades)