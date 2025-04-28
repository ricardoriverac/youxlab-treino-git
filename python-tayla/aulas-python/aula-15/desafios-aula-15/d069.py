totalMaiorIdade = 0
totalHomens = 0
totalMulher = 0

while True:
    print('\033[1m-\033[m' * 20)
    print('\033[1;33mCADASTRE UMA PESSOA\033[m')
    print('\033[1m-\033[m' * 20)

    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().strip()

    while sexo not in 'FM':
        sexo = input('Sexo: [M/F] ').upper().strip()

    #vendo quantas pessoas tem mais de 18 anos
    if idade > 18:
        totalMaiorIdade += 1

    #quantos homens foram cadastrados
    if sexo == 'M':
        totalHomens += 1

    #quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        totalMulher += 1
    
    pergunta = input('Quer cadastrar mais pessoas? [S/N] ').upper()

    while pergunta not in 'SN':
        pergunta = input('Quer cadastrar mais pessoas? [S/N] ').upper()

    if pergunta == 'N':
        break

print('\033[1m-\033[m' * 40)
print(f'O total de pessoas com mais de 18 anos cadastradas foi {totalMaiorIdade}')
print(f'O total de homens cadastrados foi de {totalHomens}')
print(f'E temos {totalMulher} mulheres com menos de 20 anos cadastradas')
print('\033[1m-\033[m' * 40)