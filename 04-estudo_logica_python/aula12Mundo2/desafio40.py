nota1=float(input('Digite sua nota:'))
nota2=float(input('Digite outra nota:'))
media=(nota1 + nota2) /2
print(f' Com a nota {nota1} e a nota{ nota2}, a média do aluno é {media}')
if media < 5.0 :
    print('Que pena vc foi REPROVADO !')
elif media > 5.0 :
    print('Que bom vc foi  APROVADO!')
elif media > 5 and media <= 6.9:
   print('Vc  esta de RECUPERAÇAO! ')
elif media > 7.0:
    print('APROVADO !!!')