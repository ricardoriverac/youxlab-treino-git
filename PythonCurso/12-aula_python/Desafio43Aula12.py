altura = float(input('Digite Sua altura '))
peso = float(input('Digite sua peso '))

imc = peso / (altura ** 2)

print('Seu IMC é de {:.1f}'.format(imc))

if imc <18.5:
    print('Você etá Abaixo do Peso!!')

elif imc <25:
    print('Você está no peso ideal!!')

elif imc <30:
    ('Você etá com Sobrepeso!!')

elif imc <40:
    print('Você está obeso!!')

elif imc >40:
    print('Você está na obesidade mórbia')

