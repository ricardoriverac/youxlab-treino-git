import datetime
conteMenorDeIdade = 0
conteMaiorDeIdade =
for pessoas in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento: '))
    anoAtual = datetime.datetime.now().year
    idade = anoAtual - nascimento
    if idade < 21:
        conteMenorDeIdade += 1
        print (f'Você tem {idade} anos de idade. Você é menor de idade!')
    elif idade <= 110:
        conteMenorDeIdade += 1
        print (f'Você tem {idade} anos de idade. Você é maior de idade!')
    if idade > 110:
        print (f'Você tem {idade} anos de idade. Esta pessoa provavelmente já morreu. ')