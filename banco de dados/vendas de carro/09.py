# O .iloc[] retorna todas as observações indexadas na posição (posição começa do 0) que escolher
import pandas as pd
dados = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/vendas de carro/venda-de-carros.csv', sep=',')
print ('-=' * 4, '\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (dados.head())
print ('-=' * 4, '\033[33m USANDO ILOC PARA LOCALIZAR POR POSIÇÃO \033[m','-=' * 4 )
print ('-=' * 4, '\033[35m observações/dados da posição 1 \033[m','-=' * 4 )
print (dados.iloc[1])
print ('-=' * 4, '\033[35m observações/dados da posição 4 até 6 \033[m','-=' * 4 )
print (dados.iloc[4:6]) # 4 e 5 
print ('-=' * 4, '\033[35m observações/dados da coluna  quilometragem 4 até 6 \033[m','-=' * 4 )
print (dados.iloc[4:6,2]) # 4 e 5 (quilometragem)
# O .loc[] faz o index acessa os rótulos dos index, se eu acessar o rótulo 4 do index:
print ('-=' * 4, '\033[33m USANDO LOC PARA LOCALIZAR POR NOME, NÚMERO A EXATA POSIÇÃO \033[m','-=' * 4 )
print ('-=' * 4, '\033[35m observações/dados da posição 4 \033[m','-=' * 4 )
print (dados.loc[4])
print ('-=' * 4, '\033[35m observações/dados da coluna 4 até 6 \033[m','-=' * 4 )
print (dados.loc[4:6]) # 4 , 5  e 6
print ('-=' * 4, '\033[35m observações/dados da coluna  quilometragem 4 até 6 \033[m','-=' * 4 )
print (dados.loc[4:6,'Quilometragem']) # 4 e 5 (quilometragem)
print ('-=' * 4, '\033[35m Seleção de múltiplas colunas: \033[m','-=' * 4 )
print (dados[['Fabricante', 'Cor', 'Portas']])
# Para deletar uma coluna use o del
print ('-=' * 4, '\033[33m DEL , DELETAR COLUNA \033[m','-=' * 4 )
del(dados['Quilometragem'])
print(dados)