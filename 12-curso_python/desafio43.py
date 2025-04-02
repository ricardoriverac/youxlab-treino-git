from time import sleep 
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
print ('CALCULANDO SEU IMC...')
sleep(2)
imc = peso / (altura * altura)
print('O seu IMC é {:.2f}'.format(imc))
if imc <18.5 :
    print('Você está abaixo do peso, coma.')
elif imc >=18.5 and imc <=25 :
    print('Seu peso está ideal! Boa.')
elif imc >=25 and imc <=30 :
    print ('Você está com sobrepeso, malhe antes que fique obeso.')
elif imc >=30 and imc <=40 :
    print('Você está obeso, vá a um nutricionista!')
elif imc >40 :
    print('Obesidade mórbida! Se cuide antes que morra!')


