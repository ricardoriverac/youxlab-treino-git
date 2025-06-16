Pessoas = []
total = []
maiorPeso = menorPeso = 0
cont = 0
pessoasPesadas = []
while True:
    nome = str(input('Digite o nome da pessoal: '))
    peso = float(input(f'Digite o peso de {nome}: '))
    Pessoas.append(nome)
    Pessoas.append(peso)
    if len(total) == 0:
        maiorPeso = menorPeso = Pessoas[1]
        cont += 1
    else:
        if Pessoas[1] > maiorPeso:
            maiorPeso = Pessoas[1]
            pessoasPesadas.append(nome)
        if Pessoas[1] < menorPeso:
            menorPeso = Pessoas[1]
    total.append(Pessoas[:])
    Pessoas.clear()
    continuar = str(input('Quer continuar? S/N: ')).upper()
    if continuar == 'N':
        break
print(f'Foram cadastradas {cont}')
print(f'O maior peso foi de {maiorPeso}kg ', end= '')
for p in total:
    if p[1] == maiorPeso:
        print(f'{p[0]} ', end= '')
print(f'O menor peso foi de {menorPeso}kg ', end='')
for p in total:
    if p[1] == menorPeso:
        print(f'{p[0]}', end='')
