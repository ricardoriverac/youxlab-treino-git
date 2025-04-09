peso= float(input('Informe seu peso: '))
altura= float(input('Informe sua altura: '))
imc= peso / (altura ** 2)
if imc < 18.5:
    print('ABAIXO DO PESO! {:.2f}'.format(imc))
elif imc >= 18.5 and 25:
    print('PESO IDEAL! {:.2f}'.format(imc))
elif imc > 25 and 30:
    print('SOBREPESO! {:.2f}'.format(imc))
elif imc >= 30 and 40:
    print('OBESIDADE! {:.2f}'.format(imc))
elif imc > 40:
    print('OBESIDADE MÓRBIDA! {:.2f}'.format(imc))