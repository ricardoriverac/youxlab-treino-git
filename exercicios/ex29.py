velocidade = float (input ("Qual a velocidade do carro ? "))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print ("Você foi multado !!")
    print ("A multa vai custar 7,0 R$ por cada KM acima do limite ! ")
    print ("O valor da multa é : {:.2f}".format(multa))
else:
    print ("Você está na velocidade permitida. BOA VIAGEM !! ")