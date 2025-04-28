valores = []
pares = []
impar = []

while True:

    numero = int(input('Digite um valor: '))

    if numero in valores:
       print('Valor duplicado! Não vou adicionar')

    else:
        print('Valor adicionado com sucesso...')
        valores.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else: 
        impar.append(numero)

    pergunta = input('Quer continuar [S/N] ').upper()

    if pergunta == 'N':
        break

print('-=' * 28)
print(f'Você digitou os valores {sorted(valores)}')
print(f'Os valores pares são: {sorted(pares)}')
print(f'Os valores ímpares são: {sorted(impar)}')