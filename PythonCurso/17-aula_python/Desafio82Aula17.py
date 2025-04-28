print('='*60)
print('Seja Bem vindo, Faça sua Lista!!')
print('='*60)


numero = list()
pares = list()
impares = list()
while True:
    numero.append(int(input('Digite um número: ' )))
    responda = ' '
    while responda not in 'SN':
        
        responda = input('Você quer continuar? [S/N] ').strip().upper()[0]

    if responda == 'N':
        break
        
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
        
        
print('='*60)
print(f'A lista completa é, {numero}')
print(f'Os números pares são, {pares}')
print(f'Os números ímpares são, {impares}')
print('='*60)
