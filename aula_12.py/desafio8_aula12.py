m = float(input('Digite seu o peso: '))
h = float(input('Digite a sua altura :'))
imc = (m / (h**2))
if imc < 18.5:
    print("Seu IMC é de: {:.2f}. Você está abaixo do peso.".format(imc))
elif imc < 25:
    print("Seu IMC é de: {:.2f}. Você está no seu peso ideal.".format(imc))
elif imc < 30:
    print("Seu IMC é de: {:.2f}. Você está com sobrepeso.".format(imc))
elif imc < 40:
    print("Seu IMC é de : {:.2f}. Você está obeso.".format(imc))
else:
    print("Seu IMC é de {:.2f}. Você está com obesidade mórbida.".format(imc))