print('-=-' * 20)
alt=float(input('Qual a sua altura ? '))
print('-=-' * 20)
peso=float(input('Seu peso?  '))
print('-=-' * 20)
imc= peso / (alt ** 2 )
print('Seu IMC e {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <25:
    print(' Peso ideal')
elif imc <30:
    print('Sobrepeso')
elif imc <40:
    print('Obesidade')
elif imc >40:
    print('Obesidade morbida')            