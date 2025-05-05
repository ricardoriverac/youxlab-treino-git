#CADASTRO DE TRABALHO
from datetime import date
pessoa={}
pessoa['nome']=str(input('Nome: '))
pessoa['ano de nascimento']=int(input('Ano de nascimento: '))
pessoa['carteira de trabalho']=int(input('Carteira de trabalho (0 não tem): '))
if pessoa['carteira de trabalho']==0:
    print(f'nome tem o valor {pessoa["nome"]}')
    print(f'idade tem o valor {date.today().year - pessoa["ano de nascimento"]}')
    print(f'Carteira de Trabalho tem o valor 0')
else:
    pessoa['ano de contratação']=int(input('Ano de contratação: '))
    while pessoa['ano de contratação'] == 0:
        print('Ano de contratação inválido! Digite um ano válido (diferente de 0).')
        pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salario']=float(input('Salário: R$'))
    anoAposentadoria=pessoa['ano de contratação']+35
print('RESULTADO:')
print(f'nome tem o valor {pessoa["nome"]}')
print(f'idade tem o valor {date.today().year - pessoa["ano de nascimento"]}')
print(f'Carteira de Trabalho tem o valor {pessoa["carteira de trabalho"]}')
if pessoa['carteira de trabalho']!=0:
    print(f'Ano de Contratação tem o valor {pessoa["ano de contratação"]}')
    print(f'Salário tem o valor R${pessoa["salario"]:.3f}')
    print(f'Aposentadoria tem o valor {anoAposentadoria - pessoa["ano de nascimento"]}')