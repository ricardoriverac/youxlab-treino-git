nota1= float(input('Digite sua primeira nota: '))
nota2= float(input('Digite sua segunda nota: '))
calculo= nota1 + nota2
resultado= calculo / 2
if resultado < 5:
    print('REPROVADO! NOTA ABAIXO DA MÉDIA {}'.format(resultado))
elif resultado == 5 or 6.9:
    print('RECUPERAÇÃO! NOTA MÉDIA {}'.format(resultado)) 
elif resultado >= 7:
    print('APROVADO! NOTA ACIMA DA MÉDIA {}'.format(resultado))