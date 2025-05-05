# Calculando média 
nota1=float(input('Sua nota do 1° semestre:'))
nota2=float(input('Sua nota do 2° semestre:'))
media=(nota1+nota2)/2
if media>=7.0:
    print(f'Média mínima é 6.0\nSua média é de {media}. APROVADO! ')
elif media>=5.0 and media<7.0:
    print(f'Média mínima é 6.0\nSua média é de {media}. RECUPERAÇÃO! ')
elif media<5.0:
    print(f'Média mínima é 6.0\nSua média é de {media}. REPROVADO! ')

