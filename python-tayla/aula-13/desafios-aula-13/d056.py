somaidades = 0
media = 0
idadeMaiorH = 0
nomeH = ''
somaMulher = 0

for c in range(1, 5):
    print('='*5, f'{c}º PESSOA', '='*5)
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [F/M]: ').upper()

    #somando idade pra media
    somaidades =  somaidades + idade

    #descobrindo e mostrando qual o homem mais velho
    if idadeMaiorH == 0 or idade > idadeMaiorH:
        idadeMaiorH = idade
    if sexo == 'M' and idade == idadeMaiorH:
        idadeMaiorH = idade
        nomeH = nome

    #descobrindo e mostrando quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        somaMulher += 1

#calculando a media
media = somaidades / 4

#mostrando resultados
print('=' * 12)
print(f'A média de idade do grupo é {media}')
print(f'O nome do homem mais velho do grupo é {nomeH}')
print(f'Tem {somaMulher} mulheres com menos de 20 anos')