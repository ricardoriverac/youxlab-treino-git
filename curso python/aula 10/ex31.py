distancia = float (input ("Qual a distância da viagem em Km  ? "))
print ("Sua viagem terá {:.2f} KM de distância.".format(distancia))
passagem = distancia * 0.50
if distancia <= 200:
    print ("Você pagará: R${:.2f}".format(passagem))
else:
    passagem = distancia * 0.40
    print ("Você pagará: R${:.2f}".format(passagem))