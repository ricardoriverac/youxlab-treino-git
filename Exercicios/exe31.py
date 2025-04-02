#Desenvolva um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de ate 200km
#E R$0,45 para viagens mais longas.

pKM = float(input("Quantos Km/h de distancia e sua viagen? "))

if pKM > 200:
    rKM = pKM * 0.50
    print("Voce irá pagar {} por sua viagem".format(rKM))
elif pKM <= 200:
    rKM = pKM * 0.45
    print("Voce irá pagar {} por sua viagem".format(rKM))
else: print("Voce não está viajando.")
