nome=str(input('Qual o seu nome?'))
nomeM=nome.lower()
if nomeM=='yuri':
    print('Olá Yuri')
    nota1=float(input('Qual foi a sua primeira nota? '))
    nota2=float(input('Qual foi a segunda nota? '))
    média=(nota1+nota2)/2
    if média>=6:
        print('Parabéns!!')
    else:
        print('Que nota ruim!!')
else:
    print('Vá embora!')