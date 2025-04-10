#índice de massa corporal
peso=float(input('Qual o seu peso?: '))
altura=float(input('Qual a sua altura?: '))
imc= peso/(altura**2)
if imc<18.5:
    print('Seu IMC é {:.1f}, VOCÊ ESTÁ ABAIXO DO PESO!'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu IMC é {:.1f}, VOCÊ ESTÁ NO PESO IDEAL!'.format(imc))
elif imc>=25 and imc<30:
    print('Seu IMC é {:.1f}, SOBREPESO!'.format(imc))
elif imc>=30 and imc<40:
    print('Seu IMC é {:.1f}, OBESIDADE!'.format(imc))
else:
    print('Seu IMC é {:.1f}, OBESIDADE MÓRBIDA!'.format(imc))


