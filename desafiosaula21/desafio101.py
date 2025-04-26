from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return(f'Com idade {idade}, \033[31mNÃO VOTA!\033[m ') 
    elif 16 <= idade <18 or idade > 65:
        return(f'Com idade {idade}, \033[33mÉ OPCIONAL!\033[m ')
    else:
        return(f'Com idade {idade}, \033[36mÉ OBRIGATÓRIO!\033[m ')
    
ano = int(input('Que ano você nasceu?: '))
print(voto(ano))
