lista = list()
pesos = []

while True:
    nome = input('Qual o seu nome? ')
    peso = float(input(f'Olá {nome}, qual é o seu peso? '))
    lista.append([nome, peso])
    pessoas = lista
    pesos = [p[1] for p in pessoas]
    maiorPeso = max(pesos)
    menorPeso = min(pesos)

    while True:
        resposta = input('Quer continuar? [S/N] ').upper()
        if resposta in 'SN':
            break
        print('Algo deu errado, tente de novo.', end = '')
    if resposta=='N':
        break

quantidadePessoas = len(pessoas)
print(f'A quantidade de pessoas cadastradas foi {quantidadePessoas}.')
print (f'Os menor peso foi {menorPeso}, e os maior peso foram {maiorPeso}.')