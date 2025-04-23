from datetime import datetime, date
dataAtual = date.today()
pessoas = {}
pessoas['Nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
pessoas['Idade'] = dataAtual.year - ano
pessoas['Carteira de trabalho'] = int(input('Carteira de trabalho: (Digite 0 se não tiver): '))
if pessoas['Carteira de trabalho'] != 0:
    pessoas['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoas['Salário'] = float(input('Salário: R$'))
    pessoas['Aposentadoria'] = pessoas['Idade'] + ((pessoas['Ano de contratação'] + 35) - dataAtual.year) 
for k, v in pessoas.items():
    print(f'\033[35m{k}\033[m é igual a \033[36m{v}\033[m')
    
