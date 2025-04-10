peso= float(input('Informe seu peso em kg: '))
altura= float(input('Informe sua altura em m: '))
imc= peso / (altura * altura)
if imc < 18.5:
    print('ABAIXO DO PESO! {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('PESO IDEAL! {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('SOBREPESO! {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('OBESIDADE! {:.1f}'.format(imc))
elif imc > 40:
    print('OBESIDADE MÓRBIDA! {:.1f}'.format(imc))