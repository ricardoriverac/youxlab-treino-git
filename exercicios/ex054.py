#terminar de fazer:
numMaiorIdade= 0
numMenorIdade= 0
for pessoa in range(1, 7+1):
    pessoa= (input('Seu nome: '))
    ano= int(input('Sua data de nascimento: '))
    numMaiorIdade= pessoa(1, 8)
    numMenorIdade= pessoa(1, 8)

    if ano >= 18:
        print('{} atingiu a maior idade'.format(numMaiorIdade))
    elif ano < 18: 
        print('{} não atingiu a maior idade'.format(numMenorIdade))
    