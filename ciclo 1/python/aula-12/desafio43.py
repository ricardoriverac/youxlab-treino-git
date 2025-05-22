print('Calculadora de IMC:')
p = float(input('Digite seu peso (kg): '))
a = float(input('Digite sua altura (metro e cm): '))
imc = p/(a*a)
print(imc)
print('Seu imc é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal! ')
elif imc > 25 and imc < 30:
    print('Você está com um peso ideal! ')
elif imc > 30 and imc < 45:
    print('Você está com um sobrepeso! ')
elif imc > 40 and imc < 60:
    print('Você está com obesiade! ')
elif imc > 90:
    print('Você está com obesidade mórbida! :')