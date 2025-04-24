peso = float(input('Digite um peso KG:'))
altura = float(input('Digite sua altura:'))
imc = peso / altura**2
print(f'A pessoa que {peso} é tem à altura de {altura} tem seu imc de {imc:.2f}')
if imc <= 18.5 :
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30 :
    print('Sobrepeso')
elif imc >= 30 and imc < 40 :
    print('Obesidade')
else:
    print('Thais Carla 2º')