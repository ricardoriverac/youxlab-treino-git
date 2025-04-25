from datetime import datetime
lista = {}
nome = lista['Nome'] = str(input('Digite seu nome: '))
ano = int(input("Seu ano de nascimento: "))
ano_Atual = datetime.now().year
idade = lista['Idade'] = ano_Atual - ano
carteiraT = int(input("Digite a carteira de trabalho"))
if carteiraT != 0:
    anoCont = lista['Ano de contratação:'] = int(input('Digite o ano de contratação: '))
    salario = lista['Salário:'] = float(input("Digite o salário: "))
    a = ano_Atual - anoCont
    anoAposenta = idade + 35
    if a < 35:
        lista['Aposentadoria'] = 'Ainda faltam', a, 'anos', 'Para', nome, 'se aposentar', anoAposenta
    elif a >= 35:
        lista['Aposentadoria'] = 'Aposentadoria aprovada', anoAposenta
print (lista)