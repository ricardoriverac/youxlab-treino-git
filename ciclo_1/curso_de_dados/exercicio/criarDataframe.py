import pandas as pd
import csv
rangeColunas = int(input("Quantas colunas vocẽ quer colocar? "))

nomesDentroColuna = []
aa = []
dados = {}
rangeLinhas = int(input(f"Quantas linhas você quer colocar nas colunas? "))

for c in range(rangeColunas):
    nomeColuna = str(input(f"Qual o nome da {c+1}a coluna? "))
    aa = []

    for i in range(rangeLinhas):
        elementoLinhas = str(input(f"O que você quer colocar na {i+1}a linha da coluna {nomeColuna} ? "))
        aa.append(elementoLinhas)

    dados[nomeColuna] = aa
import os
dataf = pd.DataFrame(dados)
arquivo_csv = 'livros.csv'

arquivoExiate = os.path.exists(arquivo_csv)

dataf.to_csv(arquivo_csv, index=False, mode='a', header=not arquivoExiate)









# for d in range(rangeLinhas):
#     elementoLinhas = str(input(f"O que você quer colocar na {d}a linha? "))
#     nomesDentroColuna.append(elementoLinhas)
    

# while True:
#     fazerData = str(input("quer fazer um data frame? S/N ")).upper()
#     while fazerData != "S" and fazerData != "N":
#         print('ERRO, tente novamente')
#         fazerData = str(input("quer fazer um data frame? S/N ")).upper()
#     if fazerData == "N":
#         break
#     else:
#         if fazerData == "S":
#             dados = []
#             rangeColunas = int(input("Quantas colunas vocẽ quer colocar? "))
#             listaColuna = []

#             for c in range (rangeColunas):
#                 nomeColuna = str(input(f"Qual o nome da {c}a coluna? "))

#                 elementoSeries = str(input(f"o quer colocar na coluna {nomeColuna}? "))
#                 listaColuna.append(elementoSeries)
#                 datfra = pd.DataFrame({
#                     nomeColuna: listaColuna,
#                 })

#                 bigData.append(datfra)
        
#         print(datfra)
        

            # estados = pd.Series(['Minas Gerais', 'Bahia', 'Rio de Janeiro'])

    # fabricantes = pd.Series(['BYD', 'Nissan', 'Toyotta'])

    # dataf = pd.DataFrame({
    #     'Estados': estados,
    #     'Fabricantes': fabricantes
    # })


    # print(dataf)
