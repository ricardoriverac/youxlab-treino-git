nota1 =float(input('Qual a sua primeira nota?  '))
nota2 =float(input('Sua segunda nota?  '))
m = (nota1 + nota2 ) / 2
if m < 5:
    print('REPROVADO!!!')
elif m >= 7:
    print('Aprovado')    
elif m >5 < 6.9 : 
    print('RECUPERAÇÂO')
