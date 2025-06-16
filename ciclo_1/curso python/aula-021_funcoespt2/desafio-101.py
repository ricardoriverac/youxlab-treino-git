from datetime import datetime
def voto(ano):
    anoAtual = datetime.now().year
    idade = anoAtual - ano
    p = ''
    if 18 <= idade <= 71:
        return print('VOTO OBRIGATÓRIO')
    elif idade < 18:
        return print('AINDA NÃO PODE VOTAR')
    elif idade > 72:
        return print('VOTO OPCIONAL')


ano = int(input('Qual o seu ano de nascimento? '))
voto(ano)
# print(f'{voto(ano)}')