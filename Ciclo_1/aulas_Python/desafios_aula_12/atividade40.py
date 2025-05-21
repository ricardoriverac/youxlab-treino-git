print('-=-=-=-=-Qual as notas dos alunos?-=-=-=-=-')
nota1 = float(input('Primeira nota? '))
nota2 = float(input('Segunda nota? '))

media = (nota1+nota2) /2

if media < 5.0:
    print('Você foi reprovado, estude mais!! (Sua nota {})'.format(media))
    
elif media > 7.0:
    print('Parabéns você foi aprovado! (Sua nota {})'.format(media))
    
else:
    print('Você ficou de recuperação, estude para a prova!! (Sua nota {})'.format(media))