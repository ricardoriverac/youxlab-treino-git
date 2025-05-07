import pandas as pd
data = pd.read_csv('python-tayla/aulas-dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(10)) # mostra as linhas
print(data.info())