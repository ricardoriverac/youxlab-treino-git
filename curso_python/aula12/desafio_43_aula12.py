peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura **2
if imc < 18.6:
    print (f'Seu IMC é de {imc:.2f}. Você está abaixo do peso. ')
elif 18.5 <= imc < 26:
    print (f'Seu IMC é de {imc:.2f}. Você está no peso ideal. ')
elif 25 <= imc < 31:
    print (f'Seu IMC é de {imc:.2f}. Você está com sobrepeso. ')
elif 30 <= imc < 41:
    print (f'Seu IMC é de {imc:.2f}. Você está com excesso de peso. ')
if imc > 40:
    print (f'Seu IMC é de {imc:.2f}. Você está com obesidade mórbida. ')