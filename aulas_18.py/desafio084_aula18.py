print('\033[38;2;255;182;193mCadastro de Pessoas com Peso\033[0m')
print('-' * 40)

pessoas = []
maior = menor = 0

while True:
    nome = input('Nome: ').strip()
    peso = float(input('Peso (kg): '))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('\n\033[38;2;255;20;147mResultado Final\033[0m')
print('-' * 40)
print(f'Total de pessoas cadastradas: {len(pessoas)}')

print(f'\n\033[38;2;255;182;193mPessoas mais pesadas ({maior}kg):\033[0m')
for p in pessoas:
    if p[1] == maior:
        print(f' - {p[0]}')

print(f'\n\033[38;2;255;20;147mPessoas mais leves ({menor}kg):\033[0m')
for p in pessoas:
    if p[1] == menor:
        print(f' - {p[0]}')
        print('\033[38;5;198m★\033[0m')