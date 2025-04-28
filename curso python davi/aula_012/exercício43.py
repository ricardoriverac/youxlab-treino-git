ps = float(input('peso em kg '))
at = float(input('altura '))
imc = ps / (at ** 2)
print(' o IMC desta pessoa é de {:.1f}' .format(imc))
if imc < 18.5:
    print('abaixo do peso. ')
elif imc < 25:
    print('peso ideal. ')
elif imc < 30:
    print('está acima do peso. ')
elif imc < 40:
    print('obeso. ')
else:
    print('obesidade mórbida. ')

