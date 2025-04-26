def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: \033[35mVOTO NEGADO.\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: \033[35mVOTO OPCIONAL.\033[m'
    else:
        return f'Com {idade} anos: \033[35mVOTO OBRIGATÓRIO.\033[m'
ano_nascimento = int(input("Em que ano você nasceu? "))
print(voto(ano_nascimento))
