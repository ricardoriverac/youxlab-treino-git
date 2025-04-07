peso = float(input('Peso de uma pessoa:'))

altura = float(input('Altura de uma pessoa:'))

imc = peso / (altura * altura)
print(peso)

if imc <= 18.5:
    print('Abaixo do peso')

elif imc >= 18.5 and imc <= 25:
    print("Peso ideal")

elif imc >= 25 and imc <= 30:
    print('Sobrepeso') 

elif imc >= 30 and imc <40: 
    print('Sobrepeso')

else: 
    print('Obesidade Mórbida')