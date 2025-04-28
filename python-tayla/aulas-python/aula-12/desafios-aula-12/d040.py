nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é {media}')
if media < 5:
    print('Você está reprovado! Ninguém mandou ser burro')
elif media >= 5 or media <= 6.9:
    print('Você está de recuperação! Estude mais')
else:
    print('Você está aprovado! Parabéns')