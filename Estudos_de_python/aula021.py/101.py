
def voto(nascimento):
    from datetime import date

    anoAtual=date.today().year

    idade = anoAtual - nascimento

    if idade <= 15:
        print('Você não precisa votar: ')


    elif idade == 16 or idade == 17:
        print('Você pode votar se quiser ')

    elif idade >= 18 and idade <= 65:
        print('Você deve votar ')

    elif idade >65:
        print('Você não precisa votar ')




voto(int(input('Digite seu ano de nascimento: ')))
