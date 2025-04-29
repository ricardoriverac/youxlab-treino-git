numero = float(input('Qual o seu salario? '))

if numero < 1.200:
    soma1 = numero*0.10
    dez = (soma1 + numero)
    print('Seu novo salario é {:.2f}'.format(dez))

else:
    soma2 = numero * 0.15
    quinze = (soma2+numero)
    
    print('Seu novo salario é {:.2f}'.format(quinze))