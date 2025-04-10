valores = []

while True:
    numero = int(input('Digite um número: '))
    valores.append(numero)

    pergunta = input('Quer continuar? [S/N] ').upper()

    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').upper()
        
    if pergunta == 'N':
        break

print('=-' * 30)
if 5 in valores:
    print('O valor 5 faz parte da lsita')
else:
    print('O valor 5 não faz parte da lista')

print(f'Você digitou {len(valores)} números')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')