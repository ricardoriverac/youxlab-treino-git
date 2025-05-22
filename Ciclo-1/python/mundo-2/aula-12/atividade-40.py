nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print(f'sua media foi {media}')
if media < 5.0:
	print('reprovado')
elif media > 5.0 and media < 6.9:
	print('recuperação')
elif media == 7.0:
	print('quase não passou')
elif media > 7.0:
	print('passou')