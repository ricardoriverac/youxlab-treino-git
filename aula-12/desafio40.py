n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
media = (n1+n2)/2
if media < 5.0:
    print('VOCÊ ESTÁ REPROVADO!')
if media >= 5.0 and media <= 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO!')
elif media >= 7.0:
    print('VOCÊ ESTÁ APROVADO!')