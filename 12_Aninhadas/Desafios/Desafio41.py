from datetime import date
ano= int(input("Insira o ano que voce nasceu: "))
atual = date.today().year
idade = atual - ano
print("O atleta tem {}anos ".format(idade))
if idade <= 9:
    print("Mirim")
elif  idade <= 15:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Sẽnior")
else:
    print("MASTER")