import datetime
conteMenorDeIdade = 0
conteMaiorDeIdade = 0
for pessoas in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento: '))
    anoAtual = datetime.datetime.now().year
    idade = anoAtual - nascimento
    if idade < 21:
        conteMenorDeIdade += 1
    elif idade <= 110:
        conteMaiorDeIdade += 1
print (f'No total, temos {conteMenorDeIdade} menores de idade e {conteMaiorDeIdade} maiores de idade. ')