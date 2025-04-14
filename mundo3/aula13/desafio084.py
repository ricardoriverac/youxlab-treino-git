pessoas = []
dado = []
pesados = []
leves = []

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maispesado = dado[1]
        maisleve = dado[1]
    if dado[1] > maispesado:
        maispesado = dado[1]
    if dado[1] < maisleve:
        maisleve = dado[1]
    
    pessoas.append(dado[:])
    dado.clear()

    r = str(input('Quer continuar (S/N)? ')).strip().upper()

    while r != 'S' and r != 'N':
        r = str(input('Quer continuar (S/N)? ')).strip().upper()
    
    if r == 'N':
        break

    print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maispesado}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maispesado:
        pesados.append(p[0])
print(f'{pesados}.')

print(f'O menor peso foi de {maisleve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maisleve:
        leves.append(p[0])
print(f'{leves}.')