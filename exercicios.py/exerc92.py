from datetime import date
lista = dict()
lista['nome'] = str(input('Nome: '))
lista['ano'] = int(input('Ano de nascimento: '))
lista['carteira'] = int(input('Carteira de trabalho (Digite 0 se não tem): '))

if lista['carteira'] != 0:
    lista['contratação'] = int(input('Ano de contratação: '))
    lista['salario'] = float(input('Salário: '))
else:
    print('Finalizado..')

lista['aposentaria'] = 62

anoAtual = date.today().year
lista['idade'] = anoAtual - lista['ano']
print(lista)
for k, v in lista.items():
    print(f'O {k} é {v} ')