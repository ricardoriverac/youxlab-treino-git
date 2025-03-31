import math
angulo=float(input("Digite o angulo que deseja: "))
seno= math.sin(math.radians(angulo))
coseno= math.cos(math.radians(angulo))
tangente= math.tan(math.radians(angulo))



print("O angulo de {}, e o que vale a Seno de {:.2f}, seu cosseno e {:.2f}, e sua Tangente e{:.2f},".format(angulo,seno,coseno,tangente))