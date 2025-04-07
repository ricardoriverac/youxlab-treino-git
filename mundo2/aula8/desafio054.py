from datetime import date
menores = 0
maiores = 0
for contagem in range(1, 8):
    pessoa = int(input(f'Digite o ano de nascimento da {contagem}ª pessoa: '))
    if date.today().year - pessoa < 18:
        menores += 1
    else:
        maiores += 1
print(f'\n{maiores} são Maiores e {menores} são menores.')