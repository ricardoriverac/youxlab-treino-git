#Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC
#e mostre seu status, de acordo com a tabela abaixo:

#abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 ate 30: Sobrepeso
#30 ate 40: Obesidade
#Acima de 40: Obesidade morbida

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = peso / altura ** 2

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 < imc < 25:
    print("Peso ideial")
elif 25 < imc < 30:
    print("Sobrepeso")
elif 30 < imc < 40:
    print("Obesidade")
else: print("Obesidade morbida")