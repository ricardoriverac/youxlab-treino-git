nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
nota= (nota1 + nota2)/2
print('A sua média foi {:.1f}'.format(nota))
if nota >= 6.0:
    print('Sua média foi boa. PARABÉNS!!')
else:
    print('Sua média não está legal...estude mais!')
    