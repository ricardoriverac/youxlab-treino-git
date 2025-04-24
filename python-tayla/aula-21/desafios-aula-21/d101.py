from datetime import datetime
idade = 0

def voto(ano):
    anoAtual = datetime.now().year
    idade = anoAtual - ano
    
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 >= idade <= 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(nascimento))