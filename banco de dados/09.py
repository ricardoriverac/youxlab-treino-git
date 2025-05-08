import pandas as pd
dados = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/vendas de carro/venda-de-carros.csv', sep=';')
print ('-=' * 4, f'\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (dados.head())
print ('-=' * 4, f'\033[35m nova coluna \033[m','-=' * 4 )
dados['Nova coluna'] = 'testando' 
print(dados)
print ('-=' * 4, f'\033[35m multiplicação da coluna \033[m','-=' * 4 )
dados['Quilometragem2'] = dados['quilometragem'] * 2
print(dados)
