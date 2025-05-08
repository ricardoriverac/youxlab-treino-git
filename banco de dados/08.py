import pandas as pd
data = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print ('-=' * 4, f'\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (data.head())
print ('-=' * 4, f'\033[35m nova coluna \033[m','-=' * 4 )
data['Nova coluna'] = 'testando' 
print(data)