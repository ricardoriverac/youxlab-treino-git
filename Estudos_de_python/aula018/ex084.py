dados =[]
principal=[]
maior = menor = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))

    if len(principal) == 0:
        maior = menor = dados[1]

    elif dados[1] > maior:
        maior = dados[1]

    elif dados[1] < menor:
        menor = dados[1]

    principal.append(dados[:])
    dados.clear()

    resposta= str(input('Quer continuar? [S/N]: ').upper())

    print( )

    if resposta == 'N':
        break

print('<!>'*20)


print(f'Foram cadastrados ao todo: {len(principal)}')
print(f'O maior peso foi de {maior}kg. Peso de ',end =' ')

for posicao in principal:
    if posicao[1] == maior:
        print(f'{posicao[0]} ',end =' ')

print( )

print(f'O menor valor e de {menor} Kg. Peso de ',end =' ')

for posicao in principal:
    if posicao[1] == menor:
        print(f'{posicao[0]} ',end =' ')


