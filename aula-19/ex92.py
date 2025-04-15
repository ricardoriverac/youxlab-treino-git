from datetime import date
dic = dict()
anoAtual = date.today().year

nome = str(input('Nome: '))
dic["nome"] = nome
anoDeNascimento = int(input('Ano de nascimento: '))
dic["anoDeNascimento"] = anoDeNascimento

carteiraDeTrabalho = int(input('Carteira de trabalho (0 não tem):'))
dic["carteiraDeTrabalho"] = carteiraDeTrabalho

anoDeContratacao = int(input('Ano de contratação: '))
dic["anoDeContratacao"] = anoDeContratacao

salario = int(input('Salário: R$'))
dic["salario"] = salario

aposentadoria = anoDeNascimento + 62
dic["aposentadoria"] = aposentadoria

idade = anoAtual - anoDeNascimento
dic["idade"] = idade

print('=-'*30)
print(f'Nome é {dic["nome"]}')
print(f'Idade é {dic["idade"]}')
if carteiraDeTrabalho == 0:
    print(f'Ctps tem o valor {dic["carteiraDeTrabalho"]}')
else:
    print(f'Ctps tem o valor {dic["carteiraDeTrabalho"]}')
    print(f'Ano de contratação é igual a {dic["anoDeContratacao"]}')
    print(f'Salário tem o valor de {dic["salario"]}')
    print(f'Ano de aposentadoria é igual {dic["aposentadoria"]}')