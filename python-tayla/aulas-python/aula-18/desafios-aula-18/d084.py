pessoas = []
pessoasPesadas = []
pessoasLeves = []
pesos = []

maiorPeso = menorPeso =  cont = 0

while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    pessoas.append(nome)
    pesos.append(peso)
    
    pergunta = input('Quer continuar? [S/N] ').upper()

    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').upper()

    if pergunta == 'N':
        break

    cont += 1
minPeso = pesos.index(min(pesos))
maxPeso = pesos.index(max(pesos)) 

for c in range(len(pessoas)) :
    if c == minPeso:
        pessoasLeves.append(pessoas[c])
    if c == maxPeso:
        pessoasPesadas.append(pessoas[c])

print('-=' * 20)
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'A pessoa mais pesada é {pessoasPesadas} com {max(pesos)}Kg')
print(f'A pessoa mais leve é {pessoasLeves} com {min(pesos)}Kg')