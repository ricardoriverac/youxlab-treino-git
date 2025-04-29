from datetime import date
ano = int(input("Ano de nascimento: "))
alist = ano + 18 
atual = date.today().year
idade = atual - ano 
print("Quem nasceu em {},tem {}anos, deve se alistar em {}, ".format(ano,idade, alist))
if alist >= idade:
    print("Voce deve se alistar ")
else:
    print("Voce nao precisa se alistar ")



