def voto(a):
    from datetime import datetime
    print('--'*20)
    ano_atual = datetime.now().year
    idade = ano_atual - a
    
    if idade <= 15:
        print(F'Com {idade} anos não é permitido votar!')
        
    if idade == 16 or idade == 17:
        print(f'Com {idade} é permitido votar, porem não obrigatorio!')
    
    if 18 <= idade <= 69:
        print(f'Se você tem {idade} anos o voto é obrigatorio!')
    
    if idade >= 70:
        print(F'O voto na idade {idade} é facultativo (opcional)!')
        

anoDeNascimento = int(input('Em que ano você nasceu?: '))
voto(anoDeNascimento)