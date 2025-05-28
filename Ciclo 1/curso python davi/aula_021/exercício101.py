from datetime import datetime
def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."
    elif 16 <= idade < 18 or idade > 70:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."
nasc = int(input("Digite o ano de nascimento: "))
resultado = voto(nasc)
print(resultado)
