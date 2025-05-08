import pandas as pd
data = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print ('-=' * 4, f'\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (data.head())
print ('-=' * 4, f'\033[35m ATRIBUINDO CONSTANTES \033[m','-=' * 4 )
print(data['PRODUTO'])
print ('-=' * 4, f'\033[35m coluna original \033[m','-=' * 4 )
produtoView = data['PRODUTO']  # retorno original da coluna PRODUTO
print (produtoView)  # a seire retornada referente a coluna, não é uma cópia mas sim uma referência a coluna do dataframe
print ('-=' * 4, f'\033[35m CÓPIA \033[m','-=' * 4 )
produtoC = data['PRODUTO'].copy() # retorna a cópia da coluna PRODUTO
print (produtoC)
print ('-=' * 4, f'\033[35m TROCANDO NOME \033[m','-=' * 4 )
data['PRODUTO'] = 'combustível' # atribuindo o valor constante 'combustível' para a linha do dataframe na coluna 'PRODUTO'
print(data['PRODUTO'])
print ('-=' * 4, f'\033[35m coluna original \033[m','-=' * 4 )
produtoView = data['PRODUTO']  # retorno original da coluna PRODUTO
print (produtoView)
print('-=' * 4, f'\033[35m coluna cópia \033[m','-=' * 4 )
print(produtoC)
