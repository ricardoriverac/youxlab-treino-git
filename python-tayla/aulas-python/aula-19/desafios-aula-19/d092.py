from datetime import datetime

dados = {}

dataAtual = datetime.now()
anoAtual = dataAtual.year

nome = input('Nome: ')
anoNascimento = int(input('Ano de Nascimento: '))
carteiraTrabalho = int(input('Cateira de Trabalho (0 não tem): '))

idade = anoAtual - anoNascimento

dados['nome'] = nome
dados['idade'] = idade
dados['ctps'] = carteiraTrabalho

if carteiraTrabalho != 0:
    anoContratacao = int(input('Ano de Contratação: '))
    salario = int(input('Salário: R$ '))
    dados['contratação'] = anoContratacao
    dados['salário'] = salario
    
    aposentadoria = anoContratacao + 35
    aposentadoria -= anoNascimento
    dados['aposentadoria'] = aposentadoria

print('-=' * 20)
for k, v in dados.items():
    print(f'{k} tem o valor de \033[1m{v}\033[m')