import random 
num = random.randint(0, 5)
n1 = int(input("Escolha um numero: "))
if n1 == num:
    print("Numero escolhido {}, Numero sorteado {}, Parabens voce ganhouu!!".format(n1,num))
else:
    print("Numero escohido {}, Numero sorteado {}, Voce perdeu".format(n1,num))