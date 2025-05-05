#ANALISADOR
somaIdade=0
mediaIdade=0
maiorIdadeMasc=0
nomeVelho=''
idadeMenorFem=0
for informacoes in range(1,5):
    print(f'{informacoes}° PESSOA')
    nome=str(input('Digite o nome:')).strip()
    idade=int(input('Digite a idade:'))
    sexo=str(input('Sexo M/F:')).strip()
    somaIdade+=idade
    if informacoes==1 and sexo in 'Mm':
        maiorIdadeMasc=idade
        nomeVelho=nome
    if sexo in 'Mm' and idade>maiorIdadeMasc:
        maiorIdadeMasc=idade
        nomeVelho=nome
    if sexo in 'Ff' and idadeMenorFem<20:
        idadeMenorFem+=1
mediaIdade= somaIdade/4
print(f'A média das idades é {mediaIdade}')
print(f'O homem mais velho tem {maiorIdadeMasc} anos e o seu nome é {nomeVelho}')
print(f'São {idadeMenorFem} mulheres abaixo de 20 anos')