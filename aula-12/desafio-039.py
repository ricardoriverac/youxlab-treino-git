from datetime import datetime

ano = int(input('Qual o ano do seu nascimento?'))
ano_atual = datetime.now().year
idade = ano_atual - ano

if idade == 18:
    print('Você ja pode se alistar no exército!')
if idade <=17:
    print('Você NÃO pode se alistar no exército!')
    print('faltam {} anos para você se alistar'.format(18 - idade))
if idade >= 19:
    print('Passou da hora de você se alistar!')
    print('Era para você ter se alistado há {} anos'.format(idade - 18))