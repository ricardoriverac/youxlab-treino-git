import pandas as pd
data = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print ('-=' * 4, f'\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (data.head())
print (data['ESTADO']) # selecionando uma coluna inteira
                       # essa forma só funciona se a varaiável não tiver, espaço,acentos etc...
print ('-=' * 4, f'\033[35m localização inteira índice 1 \033[m','-=' * 4 )
print (data.iloc[1]) # selecionando a observação indexada no índice {1} do dataframe
print ('-=' * 4, f'\033[35m  criar uma series e imprimir seu conteúdo \033[m','-=' * 4 )
print (pd.Series([5.5, 6.0,9.5])) #  criar uma Series e imprimir seu conteúdo
print ('-=' * 4, f'\033[35m  alterando nome do índice \033[m','-=' * 4 )
print(pd.Series(
    [5.5, 6.0, 9.5],
    index=['Prova 1', 'Prova 2', 'Projeto'],
    name='Notas do Luke Skywalker'
))

