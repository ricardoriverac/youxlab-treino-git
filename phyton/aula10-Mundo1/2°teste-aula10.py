nota1=float(input('Digite a nota do 1° bimestre: '))
nota2=float(input('Digite a nota do 2° bimestre: '))
media=(nota1+nota2)/2
print('A sua média é {:.1f}'.format(media))
if media>=6.0:  #se média for maior ou igual a 6.0
    print('Você passou!')   
else:
    print('Você reprovou!')
