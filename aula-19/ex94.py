dic = dict()
lista = list()
cont = mediaIdade = soma = 0

while True:
    nome = str(input('Nome: '))
    dic["nome"] = nome
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    dic["sexo"] = sexo
    if sexo == 'F':
        dic["mulheres"] = nome
    idade = int(input('Idade: '))
    dic["idade"] = idade

    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    
    cont += 1
    lista.append(dic)
    soma += idade
    mediaIdade = soma / len(lista)

    if idade > mediaIdade:
        dic["acimaDaMedia"] = nome

    if continuar != 'S':
        print('-='*35)
        print(f'Foram cadastradas {cont} pessoas.')
        print(f'A média da idade das pessoas é igual a {mediaIdade}')
        print(f'As mulheres cadastradas são, {dic["mulheres"]}')
        print(f'As pessoas com idade acima da média são {dic["acimaDaMedia"]}')

        break