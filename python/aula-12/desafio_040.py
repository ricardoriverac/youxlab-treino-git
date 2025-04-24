n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
 print(f'Sua média é {media:.2f} e você foi aprovado')
elif media < 5:
 print(f'Sua média é {media:.2f} e você foi reprovado')
else:
 print(f'Sua média é {media:.2f} e você está de recuperação')