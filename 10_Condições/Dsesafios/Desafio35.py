n1= int(input("Insira um comprimento: "))
n2= int(input("Insira outro comprimento: "))
n3= int(input("Insira o terceiro comprimento "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Esses comprimentos podem formar um triangulo ")
else:
    print("Esses comprimentos nao podem formar um triangulo")