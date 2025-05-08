# 21 Estatística descritiva
import pandas as pd
dados = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/vendas de carro/venda-de-carros.csv', sep=',')
print ('-=' * 4, '\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (dados.head())
print ('-=' * 4, '\033[35m estatística descritiva \033[m','-=' * 4 )
print(dados['Quilometragem'].describe())
print ('-=' * 4, '\033[35m calcular a média, soma, desvio padrão, min, max: \033[m','-=' * 4 )
print(dados['Quilometragem'].mean()) # média 
print(dados['Quilometragem'].sum()) # soma
print(dados['Quilometragem'].std()) # desvio padrão
print(dados['Quilometragem'].min()) # mínimo
print(dados['Quilometragem'].max()) # máximo
# Para contagem usamos .value_counts():
print ('-=' * 4, '\033[35m CONTAGEM FABRICANTE \033[m','-=' * 4 )
print(dados['Fabricante'].value_counts()) 
# Podemos também criar um novo DataFrame usando .to_frame():
print ('-=' * 4, '\033[35m DADOS FABRICANTE \033[m','-=' * 4 )
dadosFabricante = dados['Fabricante'].value_counts().to_frame().reset_index()
print(dadosFabricante)