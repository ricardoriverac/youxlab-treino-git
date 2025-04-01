#Média abaixo de 5.0 = REPROVADO
#Média entre 5.0 e 6.9 = RECUPERAÇÃO
#Média 7.0 ou maior = APROVADO

nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media= (nota1+nota2)/2
if media<5:
    print('REPROVADO')
elif media>7:
    print('APROVADO')    
else:
    print('RECUPERAÇÃO')