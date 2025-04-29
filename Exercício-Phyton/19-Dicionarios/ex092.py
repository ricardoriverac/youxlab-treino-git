from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now() .year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$ '))
    dados['aposentadorio'] = dados ['idade'] + ((dados['contratação']+ 35 ) - datetime.now().year)

print(dados)
