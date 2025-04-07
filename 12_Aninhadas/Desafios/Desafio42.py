n1= int(input("Insira um comprimento: "))
n2= int(input("Insira outro comprimento: "))
n3= int(input("Insira o terceiro comprimento "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os segmentos pode formar um triangulo")
else:
    print("Os segmentos nao podem formar um triangulo")
#obs nao terminei ainda#