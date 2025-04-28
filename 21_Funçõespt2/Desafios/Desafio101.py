def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"Com {idade} anos: voto negado"
    elif 16<= idade < 18 or idade > 65:
        return f"Com {idade } o voto e opcional"
    else:
        return f"Com {idade} o voto e obrigatorio"
nasc = int(input("Qual ano do seu nascimento: "))
print(voto(nasc))