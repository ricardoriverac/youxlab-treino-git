altura = float (input ("Qual é a sua altura? "))
peso = float (input ("Qual é o seu peso? ")) 
imc = peso / (altura * altura)
print ("Se sua ALTURA é {} , e seu PESO é {} kg, o seu IMC será {:.1f} !!".format(altura, peso,imc))
if imc < 18.5:
    print ("Abaixo do peso !")
elif imc > 18.5 and imc <25:
    print ("Peso ideal !")
elif imc > 25 and imc < 30:
    print ("Sobrepeso !")
elif imc > 30 and imc < 40:
    print ("Obessidade !")
elif imc > 40:
    print ("obesidade mórbida ! ")
