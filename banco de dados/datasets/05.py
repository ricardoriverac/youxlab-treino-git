# pacotes usados neste notebook
import pandas as pd
data = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
type(data) # é uma função embutida que serve para verificar o tipo de um objeto.
data.shape #  um atributo que mostra o formato (dimensões) de um array ou estrutura de dados.
print (f'O data Frame possui {data.shape[0]}, linhas/observações/registros e {data.shape[1]} quantidade de colunas/variáveis/')

# Criando um DataFrame
personagensDf = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70, 15, 60],
    'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
})
print ('-=' * 4, f'\033[35m TABELA \033[m','-=' * 4 )
print(personagensDf)
print ('-=' * 4, f'\033[35m INFORMAÇÕES \033[m','-=' * 4 )
print(personagensDf.info())
print ('-=' * 4, f'\033[35m NOME das colunas \033[m','-=' * 4 )
print(personagensDf.columns)
print ('-=' * 4, f'\033[35m TIPO das colunas \033[m','-=' * 4 )
print (type(personagensDf.columns))
print ('-=' * 4, f'\033[35m LISTA das colunas \033[m','-=' * 4 )
print (list(personagensDf.columns))
# RENOMER COLUNAS
print ('-=' * 4, f'\033[35m TABELA \033[m','-=' * 4 )
print(personagensDf)
print ('-=' * 4, f'\033[35m RENOMEANDO COLUNA \033[m','-=' * 4 )
print(personagensDf.rename(columns={ 'nome': 'nome completo', 'idade': 'Idade'}))
print ('-=' * 4, f'\033[35m RENOMEANDO COLUNA ORIGINAL \033[m','-=' * 4 )
print(personagensDf.rename(columns={ 'nome': 'nome completo', 'idade': 'Idade'}, inplace=True))
print(personagensDf)
