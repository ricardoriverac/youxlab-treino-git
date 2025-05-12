# executando funções para cada item de uma dataframe
import pandas as pd
data = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print ('-=' * 4, f'\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (data.head())
print ('-=' * 4, f'\033[35m funções por item \033[m','-=' * 4 )
df = pd.DataFrame ({'A': [1,2,3,4],
                    'B': [10,20,30,40],
                    'C': [100,200,300,400]},
                    index=['Linha 1', 'Linha 2', 'Linha 3', 'Linha 4'])
print(df)
print ('-=' * 4, f'\033[35m soma das linhas \033[m','-=' * 4 )
# apply() permite aplicar uma função a cada linha ou coluna de um DataFrame ou a cada elemento de uma Series.
def nossaSoma(linha):
    return linha.sum() # retorna a soma de todos valores de uma linha
resultado = df.apply(nossaSoma, axis=1)
print(resultado)
# função LAMBDA
print ('-=' * 4, f'\033[35m média \033[m','-=' * 4 )
teste = df [['A', 'B', 'C']].apply(lambda series: series.mean())
print (teste)