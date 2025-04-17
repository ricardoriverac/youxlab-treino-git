import datetime as dt

anoNasc = int(input('Ano de nascimento: '))
anoAtual = dt.datetime.today().year

def voto(anoNasc):
    idade =  anoAtual - anoNasc
    if idade < 18:
        if idade >= 16:
            resp = 'Opcional'
        else:
            resp = 'Negado'
    elif idade <= 70:
        resp = 'Obrigatório'
    else:
        resp = 'Opcional'
    print(f'Voto {resp}')
    return resp

voto(anoNasc)