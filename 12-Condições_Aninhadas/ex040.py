nota1 = float(input('primeira nota:'))

nota2 = float(input('segunda nota:'))  

d = (nota1+nota2) / 2 

if d <= 5:
    print(f'Voce foi reprovado com {d} pontos.')
elif d < 6.9:
    print(f'Está de recuperação com {d} pontos.')
else:
    d >= 7
    print(f'Voce foi aprovado com {d} pontos')