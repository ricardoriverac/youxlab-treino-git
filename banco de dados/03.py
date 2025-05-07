# pacotes usados neste notebook
import pandas as pd
data = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print ('-=' * 4, f'\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print(data)
# as 5 primeiras linhas
print ('-=' * 4, f'\033[35mAS 5 PRIMEIRAS LINHAS\033[m','-=' * 4 )
print (data.head()) # so colocar no () o número da quantidade de linhas que quer ver