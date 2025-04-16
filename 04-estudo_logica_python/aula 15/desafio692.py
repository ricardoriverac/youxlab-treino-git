mais18 = 0
homem =0
mulher20 = 0
while True:
    print('----CADASTRE UMA PESSOA----')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if perg in 'N':
        break

print(f'Existe {mais18} pessoas com mais de 18 anos.')
print(f'Existem ao todo {homem} homens cadastrados.')
print(f'Mulheres com menos de 20 anos = {mulher20}.')