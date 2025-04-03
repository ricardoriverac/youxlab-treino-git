peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura? '))
imc = peso/(altura * altura)
print('Seu IMC é {:.2f}'.format(imc))
if imc<18.5:
    print('Você está abaixo do peso ')
elif imc==18.5 or imc <=25.0:
    print('Você está no peso ideal ')
elif imc == 25 or imc <=30:
    print('Você está em sobrepeso ')
elif imc == 30 or imc <=40:
    print('Você está obeso ')
else:
    ('Você está com obesidade mórbida ')

