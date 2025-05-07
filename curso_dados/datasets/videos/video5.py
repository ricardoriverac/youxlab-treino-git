import pandas as pd
data = pd.read_csv('./curso_dados/datasets/GasPricesinBrazil_2004-2019 (1).csv')
print(data.head())
print(data.iloc[1])
notas = pd.Series([5.5, 6.0, 9.5])
notas = pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas de Juliano')
print(notas)