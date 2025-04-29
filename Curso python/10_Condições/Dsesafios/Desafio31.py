n1= int(input("Qual e a distancia da sua viagem em km? "))
p = n1 * 0.50
v = n1 * 0.45
if n1 <= 200:
    print("Sua viagem deu:{}R$".format(p))
else:
    print("Sua viagem mais longa deu:{}R$".format(v))