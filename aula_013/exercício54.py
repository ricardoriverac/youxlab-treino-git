from datetime import date
menores = 0
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da pessoa: '))
    if date.today().year - pessoa < 18:
        menores += 1
print('{} são de Maior e {} são de menores.'.format(7 - menores, menores))