def voto():
    global subtracao
    idade = int(input('Qual seu ano de nascimento? '))
    subtracao = 2025 - idade
    return idade

voto()
if subtracao >= 18:
    print(f'Você tem {subtracao} anos, VOTO OBRIGATORIO! ')
elif subtracao >= 15:
    print(f'Você tem {subtracao} anos, VOTO OPCIONAL! ')
elif subtracao < 15:
    print(F'Você tem {subtracao} anos, VOTO NEGADO')