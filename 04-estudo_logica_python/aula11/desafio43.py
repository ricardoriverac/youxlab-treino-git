peso=float(input('Qual é seu peso ? '))
altura=float(input('Qual esua altura? '))
imc=peso /(altura * altura )
if imc < 18.5:
    print("Seu IMC é de: {:.2f}. Você está abaixo do peso.".format(imc))
elif imc < 25:
    print("Seu IMC é de: {:.2f}. Você está no peso ideal.".format(imc))
elif imc < 30:
    print("Seu IMC é de: {:.2f}. Você está com sobrepeso.".format(imc))
elif imc < 40:
    print("Seu IMC é de : {:.2f}. Você está com obesidade.".format(imc))
else:
    print("Seu IMC é de {:.2f}. Você está com obesidade mórbida.".format(imc))
