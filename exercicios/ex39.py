from datetime import date
nascimento = int (input ("Qual o ano do seu nasimento: "))
anoatual = date.today().year
idade = anoatual - nascimento
print ("Quem nasceu em \033[33m{}\033[m, tem \033[36m{}\033[m anos em \033[32m{}\033[m  !".format(nascimento,idade,anoatual))
if idade == 18:
    print ("precisa alistar imediatamente!")
elif idade < 18:
    falta = 18 - idade
    print ("falta {} anos para você se alistar".format(falta))
    ano = anoatual + falta
    print ("O ano do seu alistamento será {}".format(ano))
elif idade > 18:
    falta =  idade - 18
    print ("Você já deveria ter se alistado, há {} anos".format(falta))
    ano = anoatual - falta
    print ("O ano do seu alistamento foi em {}".format(ano))
else:
    print ("Data de nascimento inválida!!")
    