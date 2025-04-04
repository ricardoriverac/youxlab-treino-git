from datetime import datetime
totalMaiores = 0
totalMenores = 0
for c in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    dataAtual = datetime.now()
    anoAtual = dataAtual.year
    idade = anoAtual - ano
    if idade >= 18:
        maiorIdade = c
        totalMaiores += 1
    else:
        menorIdade = c
        totalMenores += 1
print(f'{totalMaiores} pessoas são maiores de idade')
print(f'{totalMenores} pessoas são menores de idade')