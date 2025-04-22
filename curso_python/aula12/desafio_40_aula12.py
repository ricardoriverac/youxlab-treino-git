nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print (f'Aluna(o) REPROVADA(O). Sua média foi de {media}. ')
elif 5 <= media < 7:
    print (f'Aluna(o) em recuperação. Sua média foi de {media}. ')
elif 7 <= media <= 10:
    print (f'Aluna(o) APROVADA(O). Sua média foi de {media}. ')