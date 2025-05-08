import pandas as pd
dados = pd.read_csv('/home/youx/curso python/youxlab-treino-git/banco de dados/vendas de carro/venda-de-carros.csv', sep=',')
print ('-=' * 4, '\033[35mTABELA COMPLETA\033[m','-=' * 4 )
print (dados.head())
# O .unique() retorna os dados únicos de uma coluna
print ('-=' * 4, '\033[35m RETORNA DADOS DE UMA ÚNICA COLUNA \033[m','-=' * 4 )
print (dados['Fabricante'].unique())
# Para filtrar por condições, utilizamos .query() e no final do filtro usamos .reset_index() para os dados filtrados voltarem o index começando do 0.
print ('-=' * 4, '\033[35m RETORNA APENAS DADOS HONDA \033[m','-=' * 4 )
dadosfiltrados1 = dados.query('Fabricante == "Honda"').reset_index()
print(dadosfiltrados1)
print ('-=' * 4, '\033[35m RETORNA APENAS DADOS HONDA E AZUL \033[m','-=' * 4 )
dadosFiltrados2 = dados.query('Fabricante == "Honda" and Cor == "Azul"').reset_index()
print(dadosFiltrados2)
print ('-=' * 4, '\033[35m OUTRA FORMA DE FILTRAR \033[m','-=' * 4 )
dadosFiltrados3 = dados[dados['Fabricante'] == "Honda"]
print(dadosFiltrados3)
print ('-=' * 4, '\033[35m OUTRA FORMA DE FILTRAR P.02 \033[m','-=' * 4 )
dadosFiltrados4 = dados[(dados['Fabricante'] == "Honda") & (dados['Cor'] == "Azul")] 
print(dadosFiltrados4)
# Filtrando a partir de uma lista
print ('-=' * 4, '\033[35m Filtrando a partir de uma lista \033[m','-=' * 4 )
listaCor = ['Azul', 'Vermelho']
dadosFiltrados5 = dados.query('Cor in @listaCor')
print(dadosFiltrados5)
# O .dropna() remove todas as linhas do DataFrame que são vazias.
# O .fillna() preenche todos valores vazios de um DataFrame com 0.