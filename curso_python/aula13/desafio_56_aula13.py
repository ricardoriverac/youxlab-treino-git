somaDasIdades = 0
mediaIdadeGrupo = 0
idadeHomemVelho = 0
nomeHomemVelho = 0
totalMulheres20 = 0
for pessoas in range(1, 5):
    print (f'_____ {pessoas}ª PESSOA _____')
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Insira a idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaDasIdades += idade
    if pessoas == 1 and sexo in 'Mm':
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo in 'Mm' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulheres20 += 1
mediaIdadeGrupo = somaDasIdades / 4
print (f'A média de idade do grupo é de {mediaIdadeGrupo:.2f} anos.')
print (f'O homem mais velho se chama {nomeHomemVelho}. ')
print (f'No total, temos {totalMulheres20} mulheres com menos de 20 anos. ')