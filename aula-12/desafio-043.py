#Desenvolva uma lógica que leia o peso a altura
#de uma pessoa, calcule seu imc e mostre seu status
#de acordo com a tabela abaixo:
#- abaixo de 18.5: abaixo do peso
#- entre 18.5 e 25: peso ideal
#-25 até 30: sobrepeso
#30 até 40: obesidade
#acima de 40: obesidade morbida

peso = float(input('digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura ** 2)

print('{:.1f}'.format(imc))
if imc <= 18.4:
    print('Você esta abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal!')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')