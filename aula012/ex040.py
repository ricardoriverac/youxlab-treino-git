nota1=float(input('Me diga sua nota do primeiro Bimestre: '))
nota2=float(input('Me diga a nota do segundo Bimestre: '))
media=(nota1 + nota2)/2

if media <= 14:
    print('Você não ira passar de ano ')
elif media ==15:
    print('Foi por pouco mas você passou de ano ')
elif media <= 30:
    print('Você passou de ano com uma nota mediana') 
else:
    print('Parabens você passou de ano!!!')
