nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
media = (nota1 + nota2) / 2 
print('com a nota {:.2f} e {:.2f}, a média do aluno é {:.2f} '.format(nota1, nota2, media ))
if media < 5:
    print('notas insuficientes,REPROVADO')
elif media > 5 and media <=6.9:
    print('RECUPERAÇÃO, se esforce mais')
elif media >= 7:
    print('APROVADO')