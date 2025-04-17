from datetime import date
def voto(x=0):
    data_atual = date.today()
    resp = 'none'
    if x == 0:
        resp = 'Idade inválida!'
    elif data_atual.year-x < 16:
        resp = f'Com {data_atual.year-x} anos: NÃO VOTA.'
    elif data_atual.year-x >= 18:
        resp = f'Com {data_atual.year-x} anos: VOTO OBRIGATÓRIO.'
    elif data_atual.year-x > 65 or 16 <= data_atual.year-x < 18:
        resp = f'Com {data_atual.year-x} anos: VOTO OPCIONAL.'
    return resp
print('-'*49)
ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))