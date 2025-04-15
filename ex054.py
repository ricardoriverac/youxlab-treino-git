numMaiorIdade= 0
numMenorIdade= 0
for pessoa in range(1, 7+1):
    pessoa= (input('Seu nome: '))
    idade= int(input('Sua idade: '))
    numMaiorIdade= pessoa(1, 8)
    numMenorIdade= pessoa(1, 8)

    if idade >= 18:
        print('{} atingiu a maior idade'.format(numMaiorIdade))
    elif idade < 18: 
        print('{} não atingiu a maior idade'.format(numMenorIdade))
    