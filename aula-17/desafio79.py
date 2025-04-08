numeros = []
while True:
    numero = int(input('Digite um valor: '))
    if numero in numeros:
        print('valor duplicado! Não vou adicionar...')
    else:
        print('valor adicionado com sucesso...')
        numeros.append(numero)

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Opção Inválida!')
        else:
            break
    if continuar == 'N':
        break

print(f'valores digitados (ordem crescente): {sorted(numeros)}')