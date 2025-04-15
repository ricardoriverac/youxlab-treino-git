valores = []
while True:
    numeros = int(input('Digite um valor: '))
    valores.append(numeros)
    valores. sort(reverse=True)
    responda = ' '
    while responda not in 'SN':
        
        responda = input('Você quer continuar? [S/N] ').strip().upper()[0]

    if responda == 'N':
        break

if 5 in valores:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista! ')

print(f'Foram digitados {len(valores)}, números')
print(f'Sua lista em ordem decrescente {valores}')
    