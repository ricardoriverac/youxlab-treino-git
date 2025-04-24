def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento 

    if idade < 16:
        return f'Com {idade} anos: você \033[1;31mNÃO VOTA\033[m.'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: seu voto é \033[1;33mOPCIONAL\033[m.'
    else: 
        return f'Com {idade} anos: seu voto é \033[1;32mOBRIGATÓRIO\033[m.'

# programa principal :)
nascimento = int(input('Em qual ano você nasceu? '))
resultado = voto(nascimento)
print(resultado)