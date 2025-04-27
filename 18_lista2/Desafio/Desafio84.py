nomes = []

pesos = []

while True:

    nome = str(input('Nome: '))

    peso = float(input('Peso: '))

    nomes.append(nome)

    pesos.append(peso)

    continuar = ' '

    while continuar not in 'NS':

        continuar = str(input('Quer continuar[S/N]? ')).strip().upper()

    if continuar == 'N':

        break

print('=-' * 30)

print(f'Ao todo você cadastrou {len(nomes)} pessoas.\n'

      f'O maior peso foi de {max(pesos)} kg. Peso de {nomes[pesos.index(max(pesos))]}.\n'

      f'O menor peso foi de {min(pesos)} kg. Peso de {nomes[pesos.index(min(pesos))]}.')